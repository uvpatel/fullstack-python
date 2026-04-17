import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_routes import router as user_router




app = FastAPI()

CORSMiddleware(
    allow_origins=["https://localhost:8501"],
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    
)


app.include_router(user_router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.post("/")
async def write_root(user: str) -> object:
    return {"Hello": user}




if __name__ == "__main__":
    uvicorn.run(app=app,host="localhost",port=8000)
    
