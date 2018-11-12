import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn import metrics

f = open("features.csv","r")
data = f.readlines()
X = []
for i in data:
    t = i.strip("\n")
    t = t.split(",")
    fea = []
    fea.append((float(t[4])-1)/1.5)
    temp = float(t[5])
    if 5 < temp:
        temp = 5
    fea.append((temp-0.5)/4.5)
    temp = float(t[6])
    if temp > 10:
        temp = 10
    fea.append((temp)/10)
    X.append(fea)
y_pred = KMeans(n_clusters=2, random_state=9).fit_predict(X)
plt.scatter([t[0] for t in X], [t[2] for t in X], c=y_pred)
plt.show()