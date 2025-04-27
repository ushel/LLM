from decouple import config
from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import os


app = FastAPI()
# key_op = "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"
model = ChatOpenAI(openai_api_key=config("OPENAI_API_KEY"))
prompt = ChatPromptTemplate.from_template("Give me a summary about {topic} in a paragraph or less.")
chain = prompt | model

add_routes(app, chain, path="/openai")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)