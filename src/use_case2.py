import doc2vec
import cluster
import os

def use_case():
    doc_vecs = doc2vec.doc2vec_cluster()
    km = cluster.mbkmeans_clusters(doc_vecs, 5, 10, True)
    cluster_no = int(input("Enter cluster number: "))
    directory = '../data/issues'
    km_labels = km[1]
    # iterate over files in that directory
    count = 0
    users = []
    for filename in os.listdir(directory):
        if(km_labels[count] != cluster_no):
            count += 1
            continue
        file = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(file):
            flag = False
            with open(file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line.startswith('user:'):
                        flag = True
                        continue
                    if(line.startswith('status:') or len(line) == 0):
                        flag = False 
                    if(flag):
                        users.append(line)
        count += 1
    print(users)