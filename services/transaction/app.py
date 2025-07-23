from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/transactions/{transaction_id}")
async def get_transaction(transaction_id: str):
    return {"transaction_id": transaction_id, "status": "Completed"}

@app.post("/transactions")
async def create_transaction(data: dict):
    return {"message": "Transaction created", "data": data}