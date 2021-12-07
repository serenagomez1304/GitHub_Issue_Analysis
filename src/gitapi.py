import requests
import os
import json
from pprint import pprint

token = os.getenv('GITHUB_TOKEN')
owner = "tensorflow"
repo = "tensorflow"
query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
query_cont = f"https://api.github.com/repos/{owner}/{repo}/contributors"
params = {
    "state": "closed",
}
headers = {'Authorization': f'token {token}'}
response_issues = requests.get(query_url, headers = headers, params = params)
response_cont = requests.get(query_cont, headers = headers, params = params)

contributors = []
for contributor in response_cont.json():
    contributors.append(contributor['login'])
print(contributors)
comments_info = []
cont_info = {}
for issue in response_issues.json():
    if issue['number'] in range(53210, 53230):
        users_list = []
        comment_url = issue['comments_url']
        f = requests.get(comment_url)
        myfile = json.loads(f.text)
        comments_info.append(myfile)
        for comment in comments_info:
            if comment:
                users_list.append(comment[0]['user']['login'])
        cont_info[issue['number']] = users_list
print(cont_info)          
for key,value in cont_info.items():
    for name in value:
        if name in contributors:
            print(key,name)
    