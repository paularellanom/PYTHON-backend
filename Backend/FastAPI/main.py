from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "hola FastAPI"

@app.get("/url")
async def url():
    return {"url": "https://mouredev.com/python"}
