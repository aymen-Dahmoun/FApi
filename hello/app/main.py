from fastapi import FastAPI

from .api.router import api_router
app.include_router(api_router)


app = FastAPI(title="hello")

@app.get("/health")
async def health_check():
    return {"status": "ok"}