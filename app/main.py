from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root ():
    return {"message":"Hello"}

@app.get("/api/health")
def health_check():
    return {"status":"ok"}