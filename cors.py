from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import setting
app = FastAPI()

#Allowed Origins Front_end URL
origins = setting.origin 

app.add_middleware(
    CORSMiddleware,
    allow_origins= origins, #allowed FE
    allow_credentials = True,
    allow_methods= ["*"],
    allow_headers=["*"]
)
@app.get("/")
def home():
    return{
        "message":"CS ENABLE API"
    }
