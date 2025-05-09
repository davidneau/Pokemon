from fastapi import FastAPI
from routes import router
import psycopg2
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
import uvicorn

cur = ""
app = FastAPI()


if os.getenv("RENDER") == "true":
    DATABASE_URL = os.environ.get("DATABASE_URL")
    PORT = os.environ.get("PORT", 8000)
else:
    load_dotenv(".env")
    DATABASE_URL = os.getenv("DATABASE_URL")
    PORT = os.getenv("PORT")

print(DATABASE_URL)
print(PORT)

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


if __name__ == "__main__":
    port = int(PORT)  # fallback en local
    uvicorn.run("main:app", host="0.0.0.0", port=port)