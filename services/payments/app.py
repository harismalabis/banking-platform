from fastapi import FastAPI

app = FastAPI()

@app.post("/payments")
async def make_payment(payment: dict):
    return {"message": "Payment processed", "payment": payment}

@app.get("/payments/{payment_id}")
async def get_payment(payment_id: str):
    return {"payment_id": payment_id, "status": "completed"}