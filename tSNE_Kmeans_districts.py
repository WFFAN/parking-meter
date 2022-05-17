from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import pickle
import joblib
from copy import deepcopy
from pathlib import Path as p
import identify_weekday_list as iw
import seaborn as sns

bapa = \
p(r"D:\POLYU_dissertation\July_2021_useful\July_clustering\cluster_csv\district_cluster_csv", header=0, index_col=0)
ne_arr = np.zeros((18, 31, 288))
name_arr = np.zeros(18, dtype="U25")
i = 0
for piece in bapa.iterdir():
    ne_name = piece.stem
    df = pd.read_csv(piece, header=0, index_col=0)
    arr = df.to_numpy(dtype="float32")
    ne_arr[i, :, :] = arr
    name_arr[i] = ne_name
    i += 1
# print(ne_arr)
# print(name_arr)
print(ne_arr.shape)


#--------tSNE-----dimension reduction----------
k_arr = ne_arr.reshape(18, 8928)
perplexity=7
learning_rate=350
early_exaggeration=30
random_state = 45
tsne = TSNE(n_components=2, perplexity=perplexity,  init="random", learning_rate=learning_rate,
            early_exaggeration=early_exaggeration, random_state=random_state) # auto 200 # perplexity 300 5 50
result_tsne = tsne.fit_transform(k_arr)
k_means_data = result_tsne
print(result_tsne.shape)
df = pd.DataFrame()
df["y"] = name_arr
df["comp-1"] = result_tsne[:, 0]
df["comp-2"] = result_tsne[:, 1]

# ------Kmeans----------clustering---------
X = k_means_data
print("X.shape", X.shape)

#-----elbow figure----
def elbow(Y):
    # range(2,20)
    wcss = []
    for i in range(2, Y):
        kmeans = KMeans(n_clusters=i,
                        init='k-means++', max_iter=300, n_init=10)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    plt.figure(figsize=(10, 7))
    plt.plot(range(2, Y), wcss)
    plt.tick_params(which='major', length=5, width=0, labelsize=15)
    plt.title("The Elbow Method For Optimal k (district)", size=25)
    plt.xlabel("Number of clusters k", size=20)
    plt.ylabel("Sum of squared distances", size=20)
    plt.grid(ls="--")
    ne_na = "kmean_district_2_" + str(Y)+".png"
    save = p(r"D:\POLYU_dissertation\July_2021_useful\July_clustering\kmeans_result_tsne\figures")/ne_na
    plt.savefig(save,dpi=400)
Y=15
elbow(Y=Y)

# ----tsne-kmeans----list dataframe-----
def tskm(Y):
    result_df = pd.DataFrame()
    for i in range(2,Y):
        k=i
        kmeans = KMeans(n_clusters=k)
        kmeans = kmeans.fit(X)
        labels = kmeans.predict(X)
        centroids = kmeans.cluster_centers_
        print("labels: ")
        print(labels)
        print("centroids: ")
        print(centroids)
        co_na = "n=" + str(i)
        result_df[co_na] = np.array(labels)
    ne_na = "tskm_district_2_" + str(Y) + ".csv"
    save = p(r"D:\POLYU_dissertation\July_2021_useful\July_clustering\kmeans_result_tsne\result_kmeans_csv") / ne_na
    # print(result_df)
    result_df.to_csv(save,index=False)
# tskm(Y=Y)

# ----tsne-kmeans----draw figure-----
k = 6
kmeans = KMeans(n_clusters=k)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_
df["labels"] = labels
print("df.head()")
print(df.head())
label_na = ["cluster " + str(x) for x in labels]
df["label_na"]= label_na

plt.figure(figsize=(15,10))
hue_order = ["cluster " + str(i) for i in range(0, k)]
t_plot = sns.scatterplot(x="comp-1", y="comp-2", hue="label_na",
                hue_order=hue_order,
                palette=sns.color_palette("husl", k), s=200,
                data=df, style="label_na")# .set(title="T-SNE",size=25) # , 8
plt.xlabel("feature space $x_{1}$", size=20)
plt.ylabel("feature space $x_{2}$", size=20)
plt.title("K-means clustering (district pattern)", size=40)
plt.tick_params(which='major', length=5, width=0, labelsize=15)
plt.subplots_adjust(bottom=0.2) # to solve the legend can't show entirely
plt.legend(
        loc="upper left", bbox_to_anchor=(0.01, -0.1), ncol=3, frameon=False, handleheight=0.3,markerscale=3,
        handlelength=0, fontsize=20, title_fontsize=8, labelspacing=0.3, borderpad=0.0, columnspacing=12)
ne_na = "tskm_district"+"_k"+str(k)+"_p" + str(perplexity) + "_l" + str(learning_rate) + \
        "_e" + str(early_exaggeration)+"_r"+str(random_state) + ".png"
sa_pa = p(r"D:\POLYU_dissertation\July_2021_useful\July_clustering\kmeans_result_tsne\figures")/ne_na
plt.savefig(sa_pa,dpi=400)
