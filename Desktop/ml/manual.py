import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("customer.csv")

print(df.head())

plt.figure(figsize=(6,4))
df['purchased'].value_counts().plot(kind='bar',color=['green', 'red'])
plt.title("purchased vs not purchased ")
plt.xlabel("Purchased")
plt.ylabel("Count")
plt.show()
