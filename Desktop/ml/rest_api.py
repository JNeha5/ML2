import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/posts"
data = requests.get(url).json()

df = pd.DataFrame(data)
print(df.head())
