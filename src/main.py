import extract
import cluster

from gensim.models.keyedvectors import KeyedVectors
model_path = '../model/GoogleNews-vectors-negative300.bin'
w2v_model = KeyedVectors.load_word2vec_format(model_path, binary=True)
# print(w2v_model)

from word2vec import Word2Vec
wv = Word2Vec(w2v_model)

doc_vecs = []
for str in extract.str_list:
    word_vecs = []
    word_vecs.append(wv.vectorize(str))
    doc_vecs.append(word_vecs)

km = cluster.mbkmeans_clusters(doc_vecs, 9, 10, True)
print(km)

# print(doc_vecs)
