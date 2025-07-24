from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok"}, status_code=200)

if __name__ == "_main_":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=5001,reload= True)