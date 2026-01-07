from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="DevOps Portfolio API")

app.include_router(router)


@app.get("/health")
def health_check():
    return {"status": "ok"}
