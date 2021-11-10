import cluster
import extract


from gensim.models.keyedvectors import KeyedVectors
model_path = '../model/GoogleNews-vectors-negative300.bin'
w2v_model = KeyedVectors.load_word2vec_format(model_path, binary=True)

from word2vec import Word2Vec
wv = Word2Vec(w2v_model)

def doc2vec_cluster():
    doc_vecs = []
    for str in extract.str_list:
        word_vecs = []
        word_vecs.append(wv.vectorize(str))
        doc_vecs.append(word_vecs)
    return doc_vecs
    # km = cluster.mbkmeans_clusters(doc_vecs, 9, 10, True)
    # return km
