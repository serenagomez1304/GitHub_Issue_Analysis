import os
import cluster_related_issues
import classify

def use_case():
    from gensim.models.keyedvectors import KeyedVectors
    model_path = '../model/GoogleNews-vectors-negative300.bin'
    w2v_model = KeyedVectors.load_word2vec_format(model_path, binary=True)

    from word2vec import Word2Vec
    wv = Word2Vec(w2v_model)
    cluster_related_issues.use_case()
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
        # print(test_vector)
        prediction, km_labels = classify.knn(test_vector)
        print(prediction)
    # iterate over files in that directory
    directory = '../data/issues'
    count = 0
    files = []
    for filename in os.listdir(directory):
        # print(filename)
        if(km_labels[count] != prediction[0]):
            count += 1
            continue
        file = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(file):
            flag = False
            with open(file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('status:'):
                        flag = True
                        continue
                    if(line.startswith('labels:') or len(line) == 0):
                        flag = False 
                    if(flag and line == 'closed'):
                        file = filename.split('.')
                        files.append(file[0])
        count += 1
    print(files)