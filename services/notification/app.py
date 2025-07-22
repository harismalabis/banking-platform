from fastapi import FastAPI

app = FastAPI()

@app.post("/notify")
async def send_notification(notification: dict):
    return {"message": "Notification sent", "notification": notification}