from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "The Factory is Online", "billing_risk": "ZERO"}

@app.get("/test")
def test():
    return {"message": "Local test successful"}
