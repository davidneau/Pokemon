from fastapi import FastAPI
from routes import router
import psycopg2
from fastapi.middleware.cors import CORSMiddleware

cur = ""
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:8081"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def start_up_db(): 
    conn = psycopg2.connect("host='localhost' dbname='pokemon' user='postgres' password='Dragon-49'")
    app.cur = conn.cursor()
    
app.include_router(router)