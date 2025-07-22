from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to the Banking API Gateway"}

@app.get("/health")
async def health():
    return {"status": "ok"}