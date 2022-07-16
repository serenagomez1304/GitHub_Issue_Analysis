import numpy as np
import re

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Word2Vec:
    def __init__(self, gen_w2v_model, pre_train_w2v_model, stop_words = set(stopwords.words('english'))):
        self.gen_w2v_model = gen_w2v_model
        self.pre_train_w2v_model = pre_train_w2v_model
        self.stop_words = stop_words if stop_words is not None else []

    def vectorize(self, doc: str) -> np.ndarray:
        """
        Identify the vector values for each word in the given document
        :param doc:
        :return:
        """
        tags = {
            'NN': 20,
            'NNS': 20,
            'NNP': 20,
            'NNPS': 20,
            'VB': 10,
            'VBD': 10,
            'VDB': 10,
            'VBP': 10,
            'VBZ': 10,
            'JJ': 2,
            'JJR': 2,
            'JJS': 2,
            'RB': 1,
            'RBR': 1,
            'RBS': 1
        }
        # tag_sum = 0
        # sum = 0
        doc = doc.lower()
        words = [w for w in re.split(" |, |\n|\t|/|//|(|)", doc) if w not in self.stop_words and w != None and len(w) != 0]
        list_tagged = []
        for text in words:
            token_text = word_tokenize(text)
            list_tagged.append(nltk.pos_tag(token_text))
        word_vecs = []
        for data in list_tagged:
            word = data[0][0]
            tag = data[0][1]
            try:
                # If word exists in pre-trained model vocabulary
                if(word.isnumeric() or (word.startswith('-') and word[1:].isnumeric())):
                    #print(word)
                    continue
                # print('Word:',word)
                vec = self.pre_train_w2v_model[word]
                if(tag in tags):
                    tag_wt = tags[tag]
                else:
                    tag_wt = 0
                word_vecs.append(vec*tag_wt)
            except KeyError:
                try:
                    # If word exists in generated model vocabulary
                    vec = self.gen_w2v_model.wv[word]
                    if(tag in tags):
                        tag_wt = tags[tag]
                    else:
                        tag_wt = 0
                    word_vecs.append(vec*tag_wt)
                except:
                    # Ignore, if the word doesn't exist in the vocabulary
                    pass
        #print(word_vecs)
        # Assuming that document vector is the mean of all the word vectors
        # PS: There are other & better ways to do it.
        # print(word_vecs)
        vector = np.mean(word_vecs, axis=0)
        return vector
