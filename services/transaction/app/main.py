from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/transaction/create")
def create_transaction(data: dict):
    return {"message": "Transaction recorded", "details": data}

if _name_ == "_main_":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5005, reload=True)