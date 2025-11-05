from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return{"message": "Hello - Your API is live"}

@app.get("/greet/{name}")
def greet(name : str):
    return{"Greeting":f"HI {name}, welcome to greeting page"}