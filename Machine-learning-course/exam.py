import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import DistanceMetric


DATA = pd.read_csv('report.csv', decimal='.', delimiter=",")

pulsar_stars = DATA[((DATA.TARGET == 0) & (DATA.MIP >= 83) & (DATA.MIP <= 84)) |
                    ((DATA.TARGET == 1) & (DATA.MIP >= 83) & (DATA.MIP <= 89))]

print("Кол-во строк:", len(pulsar_stars))
print("До нормировки:", pulsar_stars.MIP.mean())

scaler = MinMaxScaler()
scaler.fit(pulsar_stars)
pulsar_stars = pd.DataFrame(scaler.transform(pulsar_stars), columns=pulsar_stars.columns)

print("После нормировки:", pulsar_stars.MIP.mean())

STAR = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]

X = pd.DataFrame(pulsar_stars.drop(["TARGET"], axis=1))
y = pd.DataFrame(pulsar_stars["TARGET"])

reg = LogisticRegression(random_state=2019, solver='lbfgs').fit(X, y.values.ravel())
for i, p in enumerate(reg.predict_proba([STAR])[0]):
    print("Вероятность отнесения к классу \"" + ("не пульсар" if i == 0 else "пульсар") + "\": ", p)

for m in ["euclidean", "manhattan"]:
    dist = DistanceMetric.get_metric(m)
    distances = [dist.pairwise(np.concatenate(([i], [STAR])))[0][1] for i in list(X.values)]

    print("Расстояние до ближайшего по метрике \"" + m + "\":", min(distances))
    
    
#SELECT * FROM pulsar_stars
#WHERE
#(TARGET = 0 AND MIP BETWEEN **** AND ****) OR
#(TARGET = 1 AND MIP BETWEEN **** AND ****)
