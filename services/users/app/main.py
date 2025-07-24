from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/users/profile")
def user_profile():
    return {"user_id": "u123", "name": "Alice", "email": "alice@example.com"}

if _name_ == "_main_":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5006, reload=True)