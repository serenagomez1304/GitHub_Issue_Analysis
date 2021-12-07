import extract
import os

from gensim.models.keyedvectors import KeyedVectors
model_path = '../model/GoogleNews-vectors-negative300.bin'
w2v_model = KeyedVectors.load_word2vec_format(model_path, binary=True)

'''
# imports needed and logging
import gzip
import gensim 
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, dirname):
        self.dirname = dirname
 
    def __iter__(self):
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                yield line.split()
 
sentences = MySentences('../data/issues/') # a memory-friendly iterator
# w2v_model = gensim.models.Word2Vec(sentences)
w2v_model.train(sentences)

# w2v_model.save('/tmp/mymodel')
# new_model = gensim.models.Word2Vec.load('/tmp/mymodel')

# model = gensim.models.Word2Vec(iter=1)  # an empty model, no training yet
# model.build_vocab(some_sentences)  # can be a non-repeatable, 1-pass generator
# model.train(other_sentences)  # can be a non-repeatable, 1-pass generator

# import gensim.downloader as api
# w2v_model = api.load("word2vec-google-news-300")  # download the model and return as object ready for use
'''

from word2vec import Word2Vec
wv = Word2Vec(w2v_model)

def doc2vec_cluster():
    doc_vecs = []
    for str in extract.str_list:
        doc_vec = wv.vectorize(str)
        doc_vecs.append(doc_vec)
        # print(len(doc_vec))
    # print(len(doc_vecs))
    return doc_vecs
    # km = cluster.mbkmeans_clusters(doc_vecs, 9, 10, True)
    # return km
