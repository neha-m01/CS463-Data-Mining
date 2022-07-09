#!/usr/bin/env python3
# CS463; Data Mining



##Number 4: K-Means Clustering
#K-Means is an algorithm that takes in a dataset and a constant
# k and returns k centroids (which define clusters of data in the
# dataset which are similar to one another).
from scipy.cluster.hierarchy import single, fcluster
from scipy.spatial.distance import pdist

