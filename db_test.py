import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from pylab import rcParams
from sklearn.decomposition import  PCA
import copy
import matplotlib.cm as cm
from sklearn.neighbors import NearestNeighbors # for selecting the optimal eps value when using DBSCAN
rcParams["figure.figsize"] = 14, 6

def findOptimalEps(n_neighbors, data):
    '''
    function to find optimal eps distance when using DBSCAN; based on this article: https://towardsdatascience.com/machine-learning-clustering-dbscan-determine-the-optimal-value-for-epsilon-eps-python-example-3100091cfbc
    '''
    neigh = NearestNeighbors(n_neighbors=n_neighbors)
    nbrs = neigh.fit(data)
    distances, indices = nbrs.kneighbors(data)
    distances = np.sort(distances, axis=0)
    distances = distances[:,1]
    plt.plot(distances)
    plt.xlabel('data')
    plt.ylabel('distances')
    plt.grid()
    plt.savefig(r"D:\machine_learning\figures\eps1.png")

# importing dataset
data =pd.read_csv(r"D:\machine_learning\csv\cluster_test_data.csv", header=0, index_col=None)
date = data.iloc[:,0].copy()
print(date)
dbscan_data = data.iloc[:, 1::].copy()
print("dbscan_data: \n", dbscan_data)
dbscan_data = dbscan_data.values.astype('float32', copy=False)
print("dbscan_data: ", dbscan_data)

# Normalize data
dbscan_data_scaler = StandardScaler().fit(dbscan_data)
dbscan_ori= dbscan_data_scaler.transform(dbscan_data)
print (dbscan_ori)

# reduce the columns to 2
pca = PCA(n_components=2)
dbscan_data = pd.DataFrame(pca.fit_transform(dbscan_ori))
# add new labels  to data frame
dbscan_data['date'] = date
dbscan_data.columns = ['x', 'y', 'date']
dbscan_data = dbscan_data[['date','x', 'y']]
print("head: ", dbscan_data.head())

print("222:", dbscan_data)

findOptimalEps(2, dbscan_data[['x','y']])
model = DBSCAN(eps=7, min_samples=2, metric='euclidean').\
    fit(dbscan_data[['x','y']])
# model = DBSCAN(eps=8, metric='euclidean').\
#     fit(dbscan_data[['x','y']])
model
# add labels to dataframe
dbscan_data['dbscan_cluster'] = model.labels_
print("head2: ", dbscan_data.head())

print(model)

# Visualize results
# seperate outliers from clustered data
# outliers_df = data[model.labels_==-1]
# clusters_df = data[model.labels_!=-1]
# colors = model.labels_
# colors_xlusters = colors[colors!=-1]
# color_outliers = "black"
## Get info about the clusters
# clusters = Counter(model.labels_)
# print("clusters: ", clusters)
# print("model.labels_", model.labels_)
# print("model.labels_==-1", data[model.labels_==-1])


# plot scatter plot of labels
n_clusters = len(np.unique(model.labels_))
colors = cm.rainbow(np.linspace(0, 1, n_clusters))
cluster_labels = list(range(min(model.labels_), n_clusters))

# Create a figure.
plt.figure(figsize=(35,50))

for color, label in zip(colors, cluster_labels):
    subset = dbscan_data[dbscan_data.dbscan_cluster == label]
    for i in subset.index:
            plt.text(subset.x[i], subset.y[i],str(subset['date'][i]), rotation=25, fontsize=25)
    plt.scatter(subset.x, subset.y, s=200, c=color, label='cluster'+str(label),alpha=0.5)
#    plt.scatter(subset.x, subset.y)
plt.legend()
plt.title('DBSCAN Clusters', fontsize=50)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.grid()
plt.savefig(r"D:\machine_learning\figures\dbscan4_eps7_min2.png")
#plt.scatter()
# Plot cluster and outliers
