import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from scipy.spatial import distance

data = pd.read_csv("report.csv")
ans = data["MIP"].mean()
print(ans)
df = data.drop("TARGET", 1)

scaler = MinMaxScaler()
df = scaler.fit_transform(df)
print(df.mean(axis=0)[0])

ans = 10000000000000000
star = [0.142, 0.324, 0.6, 0.579, 0.124, 0.302, 0.309, 0.231]
for i in range(0, 202):
    ans = min(ans, distance.euclidean(df[i], star))
print(ans)
