import requests

# URL вашего FastAPI приложения
url = 'http://127.0.0.1:8000/'

# 1. Запрос без заголовка 'username'
response_default = requests.get(url)
print("Ответ без заголовка 'username':")
print(response_default.text)  # Ожидается: "hello, Petr"

# 2. Запрос с заголовком 'username'
headers = {
    'username': 'Alex'  # Имя заголовка соответствует параметру в функции `get_username`
}

response_with_header = requests.get(url, headers=headers)
print("\nОтвет с заголовком 'username':")
print(response_with_header.text)  # Ожидается: "hello, Alex"

# 3. Запрос с заголовком 'X-Username' (альтернативный формат заголовка)
headers_alt = {
    'X-Username': 'Maria'  # FastAPI автоматически преобразует заголовки
}

response_with_header_alt = requests.get(url, headers=headers_alt)
print("\nОтвет с заголовком 'X-Username':")
print(response_with_header_alt.text)  # Ожидается: "hello, Maria"
