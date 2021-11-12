import doc2vec
import cluster

def use_case():
    doc_vecs = doc2vec.doc2vec_cluster()
    km = cluster.mbkmeans_clusters(doc_vecs, 5, 10, True)
    print(km)