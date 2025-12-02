import requests

url = "https://jsonplaceholder.typicode.com/posts"
resp = requests.get(url)
data = resp.json()
print(data[:5])