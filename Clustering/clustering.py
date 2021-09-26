import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%mattplotlib inline
plt.style.use('ggplot')
plt.rcParams('figure.figsize')=(12, 8)
from sklearn.datasets import male blobs
X, y = make_blobs(n_samples = 200, random_state = 7, centers = 5)

from sklearn.cluster import KMeans
kmeansModel = KMeans(n_clusters = 5)
kmeansModel.fit(X)

lables = kmeansModel.lables_
print(lables)
plt.scatter(X[:, 0], X[:, 1], c = labels)

criteries = []
for k in range (2, 10):
  kmeansModel = KMeans(n_clusters = k, random_state = 3)
  kmeansModel.fix(X)
  criteries .append(kmeansModel.inertia_)
  
print(criteries)

plt.plot(range(2, 10), criteries)

kmeansModel = Kmeans(n-clusters = 5, random_state = 0)
kmeansModel.fix(X)
labels = kmeansModel.lables_
plt.scatter(X[:, 0], X[:, 1], c = labels)


from sklearn.cluster import DBSCAN
clustering = DBSCAN(eps = 1.36, min_samples = 3).fit_predict(X)
print(clustering)
plt.scatter(X[:, 0], X[:, 1], c = clustering)

df = pd.read_csv('content/Mall_custemers.csv')
age_score = df[['Age', 'Spending Score 1-100']].iloc[:, :].values
plt.rcParams['figure.figsize'] = (12, 8)
plt.scatters(age_score[:, 0], age_score[:, 1])

from sklearn.cluster import KMeans
kmeansModel = KMeans(n_clusters = 4)
kmeansModel.fit(age_score)
lables = kmeansModel.labels_
print(labels)
plt.scatter(age_score[:, 0], age_score[:, 1], c = labels)

citeries = []
for k in range (2, 10):
  kmeansModel = KMeans (n_clusters, random_state = 3)
  kmeansModel.fit(age_score)
  criteries.append(kmeansModel.inertia_)
  
print(criteries)

plt.plot(range(2, 10), criteries)
kmeansModel =  KMeans (n_clusters = 4, random_state = 0)
kmeansModel.fit(age_score)
lables = kmeansModel.labels_
plt.scatter(age_score[:, 0], age_score[:, 1], c = labels)


from sklearn.cluster import DBSCAN
clustering = DBSCAN(eps = 5, min_samples = 2).fit_predict(age_score)
print(clustering)
plt.scatter(X[:, 0], X[:, 1], c = clustering)

from sklearn.cluster import DBSCAN
clustering = DBSCAN(eps = 8, min_samples = 10).fit_predict(age_score)
print(clustering)
plt.scatter(X[:, 0], X[:, 1], c = clustering)
