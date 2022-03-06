import pandas as pd

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import NearestNeighbors
csv = pd.read_csv("C:\\Users\\ahmed\\Desktop\\pyprojects\\adult.csv")

x = pd.DataFrame(csv[['age', 'income']]).to_numpy()
y=[10,10] # select the point from here
model=NearestNeighbors(n_neighbors=40).fit(x)
points=model.kneighbors([y])

x_drow=[]
y_drow=[]
for rb in range(0,len(points[1][0])):
   
    x_drow.append(x[points[1][0][rb]][0])

    y_drow.append(x[points[1][0][rb]][1])
   
   
nomber=0
for sc in x[:20]:

    plt.scatter(x_drow[nomber], y_drow[nomber],marker="o")
    plt.scatter(sc[0],sc[1],c="black")
    nomber+=1
plt.scatter(y[0], y[1],marker="X")

plt.show()
