import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
response_json = response.json()
print(response_json)