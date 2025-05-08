from fastapi import FastAPI
from routes import router
import psycopg2
from fastapi.middleware.cors import CORSMiddleware
import os

cur = ""
app = FastAPI()

DATABASE_URL = os.environ.get("DATABASE_URL")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def start_up_db(): 
    conn = psycopg2.connect(DATABASE_URL)
    app.conn = conn
    app.cur = conn.cursor()

app.include_router(router) 