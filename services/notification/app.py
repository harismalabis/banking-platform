from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/notifications/{user_id}")
async def get_notifications(user_id: str):
    return {"user_id": user_id, "notifications": ["Email sent", "SMS sent"]}

@app.post("/notifications")
async def send_notification(payload: dict):
    return {"message": "Notification sent", "payload": payload}