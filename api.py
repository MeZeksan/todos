from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return { "message": "Hello, My name is Bulat Zakirov IVT-432b!"}