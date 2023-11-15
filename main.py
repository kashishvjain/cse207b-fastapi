from fastapi import FastAPI
from typing import List
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Data(BaseModel):
   data :str = Field(None, title="hacking data", max_length=1000)

@app.post("/data/")
async def get_data(s1: Data):
   print(s1)
   return s1
