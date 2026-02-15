import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv("cpu_usage.csv")

df["cpu"] = df["cpu"].astype(int)
df["time"] = range(len(df))

X = df[["time"]]
y = df["cpu"]

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("cpu_model.pkl", "wb"))

print("Model trained successfully")
