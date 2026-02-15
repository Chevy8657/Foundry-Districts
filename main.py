from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "The Factory is Online", "billing_risk": "ZERO"}

@app.get("/test")
def test():
    return {"message": "Local test successful"}
@app.get("/greet/{name}")
async def greet_user(name: str):
    return {"message": f"Hello {name}, the Factory has processed your request.", "status": "Success"}