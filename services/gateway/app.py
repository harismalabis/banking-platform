from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/gateway/status")
async def gateway_status():
    return {"message": "Gateway is active"}

@app.post("/gateway/route")
async def route_request(data: dict):
    return {"message": "Request routed successfully", "data": data}