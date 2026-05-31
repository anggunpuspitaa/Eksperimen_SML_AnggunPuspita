import pandas as pd
import os

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

os.makedirs("dataset_raw", exist_ok=True)

df = pd.read_csv(url)

df.to_csv("dataset_raw/titanic.csv", index=False)

print("Dataset Titanic berhasil disimpan")