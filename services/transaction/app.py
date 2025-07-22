from fastapi import FastAPI

app = FastAPI()

@app.get("/transactions/{transaction_id}")
async def get_transaction(transaction_id: str):
    return {"transaction_id": transaction_id, "amount": 250.0, "status": "completed"}

@app.post("/transactions")
async def create_transaction(transaction: dict):
    return {"message": "Transaction created", "transaction": transaction}