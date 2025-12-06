from fastapi import FastAPI
from lda.summary import full_summary
# from lda.llm import llm_debug
# from dotenv import load_dotenv


# load_dotenv()

app = FastAPI()

@app.get('/')
def to_check():
    return ('Hello')

@app.get("/summary")
def get_summary():
    return full_summary()

# @app.get("/debug")
# def debug():
#     return {"analysis": llm_debug(full_summary())}