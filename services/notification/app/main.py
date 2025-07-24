from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/notification/send")
def send_notification(data: dict):
    return {"message": "Notification sent", "data": data}

if _name_ == "_main_":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5003, reload=True)