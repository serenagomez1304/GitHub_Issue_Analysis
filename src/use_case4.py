import os
import use_case1
import classify

def use_case():
    from gensim.models.keyedvectors import KeyedVectors
    model_path = '../model/GoogleNews-vectors-negative300.bin'
    w2v_model = KeyedVectors.load_word2vec_format(model_path, binary=True)

    from word2vec import Word2Vec
    wv = Word2Vec(w2v_model)
    use_case1.use_case()
    new_issue = input("Enter path to issue: ")
    # checking if it is a file
    if os.path.isfile(new_issue):
        data = []
        flag=False
        with open(new_issue,'r') as f:
            for line in f:
                if line.startswith('title:') or line.startswith('labels:') or line.startswith('description:'):
                    flag=True
                    continue
                if line.strip().startswith('user:'):
                    flag=False
                if flag:
                    data.append(line)
        str = ''.join(data)
        test_vector = wv.vectorize(str)
        print(test_vector)
        prediction = classify.knn(test_vector)
        print(prediction)