import csv
import numpy as np
from numpy import linalg as LA
import matplotlib.pyplot as plt
sheet = list(csv.reader(open("13_36.csv")))
a = np.array(sheet)
a = a.astype(np.float)
k = a.mean(axis=0)
for i in range(0, 60):
    a[i] -= k

a_t = a.transpose()

F = np.array(a_t.dot(a))
Q = F * (1/60)

wb, vb = LA.eigh(Q)

Fi = np.array([vb[:, 9],vb[:, 8]]).transpose()
f = np.array(vb[:, 9]).transpose()
print(a.dot(Fi)[0][0], a.dot(Fi)[0][1])

Z = a.dot(Fi)
print((wb[8] + wb[9])/wb.sum())
print((wb[8] + wb[9] + wb[7] + wb[6])/wb.sum())

plt.scatter(Z[:, 0], Z[:, 1], edgecolor='none', s=40,cmap='winter')

#part 2
#import numpy as np 

#import matplotlib
#import matplotlib.pyplot as plt

#scores = np.genfromtxt('X_reduced_536.csv', delimiter=';')
#loadings = np.genfromtxt('X_loadings_536.csv', delimiter=';')

#values = np.dot(scores,loadings.T)

#plt.imshow(values, cmap='Greys_r')
