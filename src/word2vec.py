import numpy as np
import nltk
import re

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class Word2Vec:
    def __init__(self, w2v_model, stop_words = set(stopwords.words('english'))):
        self.w2v_model = w2v_model
        self.stop_words = stop_words if stop_words is not None else []

    def vectorize(self, doc: str) -> np.ndarray:
        """
        Identify the vector values for each word in the given document
        :param doc:
        :return:
        """
        doc = doc.lower()
        words = [w for w in re.split(" |, |\n|\t", doc) if w not in self.stop_words and len(w) != 0]
        list_tagged = []
        #char_list = [':','[',']','(',')','?','/','>','<','!','#','+','.',',']
        for text in words:
            #if(text in char_list or text.startswith('-') or text.startswith('/') or text[1:].isnumeric()):
                #continue
            token_text = word_tokenize(text)
            list_tagged.append(nltk.pos_tag(token_text))
        word_vecs = []
        for data in list_tagged:
            word = data[0][0]
            tag = data[0][1]
            try:
                if(word.isnumeric() or (word.startswith('-') and word[1:].isnumeric())):
                    #print(word)
                    continue
                vec = self.w2v_model[word]
                word_vecs.append((vec[0],tag))
                # tagged = nltk.pos_tag(word_vecs)
                # print(tagged)
            except KeyError:
                # Ignore, if the word doesn't exist in the vocabulary
                pass
        #print(word_vecs)
        # Assuming that document vector is the mean of all the word vectors
        # PS: There are other & better ways to do it.
        #vector = np.mean(word_vecs, axis=0)
        return word_vecs
        #return vector

    # def _cosine_sim(self, vecA, vecB):
    #     """Find the cosine similarity distance between two vectors."""
    #     csim = np.dot(vecA, vecB) / (np.linalg.norm(vecA) * np.linalg.norm(vecB))
    #     if np.isnan(np.sum(csim)):
    #         return 0
    #     return csim

    # def calculate_similarity(self, source_doc, target_docs=None, threshold=0):
    #     """Calculates & returns similarity scores between given source document & all
    #     the target documents."""
    #     if not target_docs:
    #         return []

    #     if isinstance(target_docs, str):
    #         target_docs = [target_docs]

    #     source_vec = self.vectorize(source_doc)
    #     results = []
    #     for doc in target_docs:
    #         target_vec = self.vectorize(doc)
    #         sim_score = self._cosine_sim(source_vec, target_vec)
    #         if sim_score > threshold:
    #             results.append({"score": sim_score, "doc": doc})
    #         # Sort results by score in desc order
    #         results.sort(key=lambda k: k["score"], reverse=True)

    #     return results