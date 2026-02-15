import pickle
import pandas as pd

model = pickle.load(open("cpu_model.pkl", "rb"))

future_time = [[100]]

prediction = model.predict(future_time)

print("Predicted CPU usage:", prediction[0], "m")
