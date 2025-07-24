from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/payments/process")
def process_payment(data: dict):
    return {"message": "Payment processed", "amount": data.get("amount", 0)}

if _name_ == "_main_":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5004, reload=True)