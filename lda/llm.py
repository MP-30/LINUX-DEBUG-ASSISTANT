from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"
    )

def llm_debug(summary):
    prompt = f"""
    You are a Linux debugging assistant.
    Analyze this system summary and list:
    1. The most likely issues
    2. Suggested fixes
    3. Commands to run
    
    System Summary:
    {summary}
    """
    response = client.chat.completions.create(
        model="google/gemma-3-1b", 
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

if __name__ == '__main__':
    print(llm_debug("CPU 90%, RAM almost full, docker unhealthy"))
