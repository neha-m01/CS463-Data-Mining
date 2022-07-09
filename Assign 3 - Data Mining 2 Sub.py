#!/usr/bin/env python
# coding: utf-8

# In[104]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from sklearn.cluster import OPTICS, cluster_optics_dbscan
import pandas as pd

##Using https://github.com/christianversloot/machine-learning-articles/blob/main/performing-optics-clustering-with-python-and-scikit-learn.md
##For reference


# In[105]:




X = pd.read_excel("Assign 3-Q2-dataset.xlsx",engine = 'openpyxl')
num_samples_total = len(X)
epsilon = 1.20
min_samples = 2
cluster_method = 'dbscan'
metric = 'euclidean'
max_eps = 2


# Compute OPTICS
db = OPTICS(max_eps=epsilon, min_samples=min_samples, cluster_method=cluster_method, metric=metric).fit(X)
labels = db.labels_


# Generate scatter plot for training data
colors = list(map(lambda x: '#FF33FA' if x == 1 else '#33A3FF', labels))
plt.scatter(X['X'], X['Y'], c=colors, marker="o", picker=True)
plt.title(f'OPTICS clustering')
plt.xlabel('Axis X[0]')
plt.ylabel('Axis X[1]')
plt.show()


# In[106]:


reachability = db.reachability_[db.ordering_]
   
core = db.core_distances_[db.ordering_]
frame = pd.DataFrame(reachability, columns = ['A'])
control = pd.DataFrame(core, columns = ['A'])

for i in range(len(X['X'])):
    print(i+1,"("+str(X['X'][i])+","+str(X['Y'][i])+')',df['A'][i])
    
plt.plot(reachability)
plt.title('Reachability')
plt.show()


# In[ ]:





# In[ ]:




