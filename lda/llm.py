import os
import httpx
import chromadb
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

# Configuration
LM_STUDIO_URL = os.getenv("LM_STUDIO_URL", "http://localhost:1234/v1")
CAMBER_API_KEY = os.getenv("CAMBER_API_KEY")
CAMBER_AGENT_TAG = os.getenv("CAMBER_AGENT_TAG", "@username.linux_debugger")

# Async client for local LM Studio
lm_studio_client = AsyncOpenAI(
    base_url=LM_STUDIO_URL,
    api_key="lm-studio"
)


def _get_relevant_runbooks(summary_text: str) -> str:
    """Queries local ChromaDB for matching troubleshooting runbooks."""
    try:
        client = chromadb.PersistentClient(path="./chroma_db")
        collection = client.get_or_create_collection(name="linux_runbooks")

        results = collection.query(
            query_texts=[summary_text],
            n_results=2
        )
        if results and results.get("documents") and results["documents"][0]:
            return "\n\n---\n\n".join(results["documents"][0])
    except Exception as e:
        print(f"[WARN] ChromaDB lookup failed: {e}")

    return "No matching troubleshooting runbooks found."


async def _call_local_lm_studio(summary: str, runbooks: str) -> str:
    """Sends RAG-augmented prompt to local LM Studio using AsyncOpenAI."""
    prompt = f"""
    You are an expert AIOps Linux diagnostic engineer.

    RETRIEVED TROUBLESHOOTING RUNBOOKS:
    {runbooks}

    CURRENT SYSTEM SUMMARY:
    {summary}

    Based on the retrieved runbooks and live system summary:
    1. Identify the most likely root cause.
    2. Provide step-by-step fix recommendations.
    3. Output exact, safe Linux/Docker bash commands to execute.
    """

    response = await lm_studio_client.chat.completions.create(
        model="google/gemma-3-1b",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


async def _call_camber_agent(summary: str) -> str:
    """Fallback handler calling Camber Cloud Agent API."""
    url = "https://camber-mcp.cambercloud.com/mcp"
    headers = {
        "Authorization": f"Bearer {CAMBER_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "agent_tag": CAMBER_AGENT_TAG,
        "message": f"Analyze this system summary and provide diagnostic fixes:\n\n{summary}"
    }

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data.get("reply", response.text)


async def llm_debug(summary: str) -> str:
    """Primary entry point: Performs local RAG + local inference with Camber Cloud fallback."""
    runbooks = _get_relevant_runbooks(summary)

    try:
        return await _call_local_lm_studio(summary, runbooks)
    except Exception as local_err:
        print(f"[WARN] Local LM Studio failed ({local_err}).")

        if CAMBER_API_KEY:
            print("[INFO] Falling back to Camber Cloud Agent...")
            return await _call_camber_agent(summary)

        raise RuntimeError("Both Local LM Studio and Camber Cloud endpoints were unreachable.")


if __name__ == '__main__':
    import asyncio


    async def test():
        test_summary = "CPU 90%, RAM almost full, docker unhealthy exit code 137"
        result = await llm_debug(test_summary)
        print(result)


    asyncio.run(test())