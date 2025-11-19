from fastapi import FastAPI
import os 
import psycopg2

app=FastAPI()

@app.get('/health')
async def main():
    return {
        "user":os.getenv("APP_ENV"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL"),
        "DB_USER": os.getenv("username")
            }

@app.get('/api/hello')
async def get_response():
    return {"message":"Hello from fastapi"}

@app.get('/api/dbcheck')
async def db_response():
    try:
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )
        cur = conn.cursor()
        cur.execute("SELECT NOW();")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return {"db_connection": "success", "time": result[0]}
    except Exception as e:
        return {"db_connection": "failed", "error": str(e)}
