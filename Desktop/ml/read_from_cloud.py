import gdown
import pandas as pd

file_id = "1vfk1Oab3KtD4-gy21rYR4yJOVe2KLso-"
url = f"https://drive.google.com/uc?export=download&id={file_id}"


# Downloads the real CSV (bypasses virus warning page)
gdown.download(url, "data.csv", quiet=False)

# Now load it with pandas
df = pd.read_csv("data.csv")
print(df.head())
