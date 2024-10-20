from fastapi import FastAPI, Body, Header, Depends, Query, HTTPException
import uvicorn
from fastapi.testclient import TestClient
import requests
app = FastAPI()

def get_username(username: str = Query('Petr')):
    if len(username) < 2:
        raise HTTPException(
            status_code=400,
            detail = 'Имя должно содержать больше 1 буквы '
        )
    if any(char.isdigit() for char in username):
        raise HTTPException(
            status_code=400,
            detail="Имя не должно иметь цифры "
        )
    
    return username

@app.get('/')
def say_hello(username: str = Depends(get_username)):
    return f'hello, {username}'

client = TestClient(app)
def test_run():
    print("тест get запроса на '/' с параметров username = 'Anna'")
    response_test = client.get('/?username=Anna')
    print(response_test.status_code)
    print(response_test.text)
if __name__ == "__main__":
    test_run()
    uvicorn.run(
        'main:app',
        host ='',
        port = 8000,
        reload = True
    )
