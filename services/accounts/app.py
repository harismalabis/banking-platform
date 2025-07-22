from fastapi import FastAPI

app = FastAPI()

@app.get("/accounts/{account_id}")
async def get_account(account_id: str):
    return {"account_id": account_id, "balance": 1000.0}

@app.post("/accounts")
async def create_account(account: dict):
    return {"message": "Account created", "account": account}