from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/payments/{payment_id}")
async def get_payment(payment_id: str):
    return {"payment_id": payment_id, "status": "Success"}

@app.post("/payments")
async def create_payment(payment: dict):
    return {"message": "Payment processed", "payment": payment}