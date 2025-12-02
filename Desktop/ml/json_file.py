import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
data = response.json()   # convert to python list/dict

# Print first 3 items
for item in data[:3]:
    print(json.dumps(item, indent=4))
