from fastapi import FastAPI
from backend.api.routes import reports

app = FastAPI()

app.include_router(reports.router)


@app.get("/")
def root():
    return {"message": "API is running"}

