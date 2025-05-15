from fastapi import FastAPI, HTTPException
from pydantic_settings import BaseSettings
import uvicorn

# Configuration via .env
class Settings(BaseSettings):
    app_name: str = "Calculator API"
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()

# Logique métier : opérations de calcul
def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b

# App FastAPI
app = FastAPI(title=settings.app_name)

@app.get("/")
def read_root():
    return {"message": f"{settings.app_name} is running in {settings.environment} mode"}
c
@app.get("/add")
def add_route(a: float, b: float):
    return {"result": add(a, b)}

@app.get("/subtract")
def subtract_route(a: float, b: float):
    return {"result": subtract(a, b)}

@app.get("/multiply")
def multiply_route(a: float, b: float):
    return {"result": multiply(a, b)}

@app.get("/divide")
def divide_route(a: float, b: float):
    try:
        result = divide(a, b)
        return {"result": result}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@app.get("/test")
def test():
    return {"message": "Test route works!"}


# Pour lancer directement avec python main.py
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
