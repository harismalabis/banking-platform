from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id, "name": "John Doe"}

@app.post("/users")
async def create_user(user: dict):
    return {"message": "User created", "user": user}