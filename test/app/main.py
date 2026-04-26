from fastapi import FastAPI

from .api.router import api_router



from .core.database import init_db



app = FastAPI(title="test")

app.include_router(api_router)




@app.on_event("startup")
async def startup_event():
    await init_db()



@app.get("/health")
async def health_check():
    return {"status": "ok"}