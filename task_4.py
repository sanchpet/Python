import pandas as pd
train_data = pd.read_csv("2.csv", delimiter=',', index_col='id')
train_data
X = pd.DataFrame(train_data.drop(['Class'], axis=1))
y = pd.DataFrame(train_data['Class']).values.ravel()
from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier(n_neighbors=3, p=1 #или2 если евклид)
neigh.fit(X, y)
NewObject = [67, 36]
neigh.predict([NewObject])
neigh.predict_proba([NewObject])
neigh.kneighbors([NewObject])
