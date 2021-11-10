from sklearn.neighbors import KNeighborsClassifier
import doc2vec
import cluster
import numpy as np

def knn(test):
    model = KNeighborsClassifier(n_neighbors = 3)
    train_vector = doc2vec.doc2vec_cluster()
    km = cluster.mbkmeans_clusters(train_vector, 9, 10, True)
    # print(km[1])
    model.fit(train_vector, km[1])
    predictions = model.predict([[test]])
    return predictions