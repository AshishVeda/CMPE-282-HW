from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the /home endpoint


@app.get("/home")
async def read_root():
    return {"message": "Hello, World!"}
