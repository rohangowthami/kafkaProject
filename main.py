from fastapi import FastAPI

import os 

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": f"From: {os.environ.get('ENV', 'DEFAULT_ENV')}"}

@app.get("/ready")
def readiness_probe():
    return {"status": "ready"}

@app.get("/health")
def liveness_probe():
    return {"status": "healthy"}
