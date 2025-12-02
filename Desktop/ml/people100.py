import pandas as pd

# Correct URL
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"

# Load CSV from web
df = pd.read_csv(url)

# Preview
print("Dataset shape:", df.shape)
print(df.head())