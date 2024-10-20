from fastapi import FastAPI
from routers import tasks
app = FastAPI()

app.include_router(tasks.router)

@app.get('/')
def root():
    return f'Hello,my friend this is app for time managment!'
