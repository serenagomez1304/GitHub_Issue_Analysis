from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import extract
import os
import string
import re
from gensim.models.keyedvectors import KeyedVectors

from gensim.models.keyedvectors import KeyedVectors
model_path = '../model/GoogleNews-vectors-negative300.bin'
pre_trained_w2v_model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# imports needed and logging
import gzip
import gensim 
import logging

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class MySentences(object):
    def __init__(self, dirname, stop_words = set(stopwords.words('english'))):
        self.dirname = dirname
        self.stop_words = stop_words if stop_words is not None else []
 
    def iterate(self):
        sentences = []
        for fname in os.listdir(self.dirname):
            for line in open(os.path.join(self.dirname, fname)):
                tokens = word_tokenize(line)
                tokens = [w.lower() for w in tokens]
                table = str.maketrans(string.punctuation, ' '*len(string.punctuation))
                stripped = [w.translate(table) for w in tokens]
                alpha_words = [word for word in stripped if not(word.isnumeric() or (word.startswith('-') and word[1:].isnumeric()))]
                words = [w for w in alpha_words if not w in self.stop_words and len(w) != 0]
                if(len(words) != 0):
                    sentences.append(words)
        # print(sentences)
        return sentences

obj = MySentences('../data/issues/') # a memory-friendly iterator
# print('print obj')
# print(obj)
sentences = obj.iterate()
# lines = []
# my_iter = iter(sentences)
# for line in my_iter:
#     lines.append(line)
# print('print sentences')
# print(lines)
# print(sentences)
model = gensim.models.Word2Vec(sentences=sentences, vector_size=300)
model.save("word2vec.bin")
generated_w2v_model = KeyedVectors.load("word2vec.bin")

# print('W2V:', w2v_model)
from word2vec import Word2Vec
wv = Word2Vec(generated_w2v_model, pre_trained_w2v_model)

# print(w2v_model.wv.most_similar('tensorflow'))
# print(w2v_model.wv.similar_by_word('serena'))

# words = list(w2v_model.wv.vocab)
# print('Vocab size: ', len(words))
# w2v_model.train(sentences)

# w2v_model.save('/tmp/mymodel')
# new_model = gensim.models.Word2Vec.load('/tmp/mymodel')

# model = gensim.models.Word2Vec(iter=1)  # an empty model, no training yet
# model.build_vocab(some_sentences)  # can be a non-repeatable, 1-pass generator
# model.train(other_sentences)  # can be a non-repeatable, 1-pass generator

# import gensim.downloader as api
# w2v_model = api.load("word2vec-google-news-300")  # download the model and return as object ready for use

def doc2vec_cluster():
    doc_vecs = []
    # stop = 0
    for str in extract.str_list:
        # if(stop == 2):
        #     break
        # stop += 1
        doc_vec = wv.vectorize(str)
        doc_vecs.append(doc_vec)
    # print(doc_vecs)
    return doc_vecs
