# import required module
import os
# assign directory
directory = '../data/issues'
 
# iterate over files in
# that directory
str_list = []
for filename in os.listdir(directory):
#     if filename not in ['3.txt', '15.txt', '16.txt', '18.txt']:
#         continue
    file = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(file):
        data = []
        flag=False
        # print(file)
        with open(file,'r') as f:
            for line in f:
                if line.startswith('title:') or line.startswith('labels:') or line.startswith('description:'):
                # if line.startswith('title:') or line.startswith('description:'):
                    flag=True
                    continue
                if line.strip().startswith('user:'):
                    flag=False
                if flag:
                    data.append(line)
        str = ''.join(data)
        str_list.append(str)
