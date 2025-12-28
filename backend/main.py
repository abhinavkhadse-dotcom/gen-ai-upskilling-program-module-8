from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

@app.get("/square/{num}")
def square_number(num: int):
    return {"number": num, "square": num**2}
