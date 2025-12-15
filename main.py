from fastapi import FastAPI
from lda.summary import full_summary
from lda.llm import llm_debug
# from dotenv import load_dotenv


# load_dotenv()

app = FastAPI()

@app.get('/')
async def to_check():
    return ('Hello')

@app.get("/summary")
async def get_summary():
    return await full_summary()

@app.get("/debug")
def debug():
    return {"analysis": llm_debug(full_summary())}