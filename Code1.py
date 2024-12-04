import requests

# Задание 1: Получение данных

# URL для поиска репозиториев с HTML кодом на GitHub
url_github = "https://api.github.com/search/repositories"
params_github = {'q': 'html'}  # Параметр поиска для репозиториев с кодом html

response_github = requests.get(url_github, params=params_github)

# Статус-код и содержимое ответа в формате JSON
print("Задание 1: Получение данных")
print(f"Статус-код ответа GitHub API: {response_github.status_code}")
if response_github.status_code == 200:
    data_github = response_github.json()
    print("Содержимое ответа в формате JSON (GitHub):")
    print(data_github)
else:
    print("Ошибка при получении данных с GitHub.")
print("\n")

# Задание 2: Параметры запроса

# URL для фильтрации записей по userId
url_jsonplaceholder = "https://jsonplaceholder.typicode.com/posts"
params_jsonplaceholder = {'userId': 1}

response_jsonplaceholder = requests.get(url_jsonplaceholder, params=params_jsonplaceholder)

# Статус-код и распечатка полученных записей
print("Задание 2: Параметры запроса")
print(f"Статус-код ответа JSONPlaceholder API: {response_jsonplaceholder.status_code}")
if response_jsonplaceholder.status_code == 200:
    data_jsonplaceholder = response_jsonplaceholder.json()
    print("Полученные записи для userId = 1:")
    for record in data_jsonplaceholder:
        print(f"Title: {record['title']}")
        print(f"Body: {record['body']}")
        print("-" * 40)
else:
    print("Ошибка при получении данных с JSONPlaceholder.")
print("\n")

# Задание 3: Отправка данных

# URL для отправки POST-запроса
url_post = "https://jsonplaceholder.typicode.com/posts"
new_data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

response_post = requests.post(url_post, json=new_data)

# Статус-код и распечатка содержимого ответа
print("Задание 3: Отправка данных")
print(f"Статус-код ответа на POST-запрос: {response_post.status_code}")
if response_post.status_code == 201:  # Проверяем, что ресурс был создан
    print("Содержимое ответа (данные, которые были отправлены):")
    print(response_post.json())
else:
    print("Ошибка при отправке данных через POST-запрос.")
