import requests
import os
import json
from pprint import pprint

token = os.getenv('GITHUB_TOKEN','...')
owner = "tensorflow"
repo = "tensorflow"
query_url = f"https://api.github.com/repos/{owner}/{repo}/issues"
params = {
    "state": "closed",
}
headers = {'Authorization': f'token {token}'}
response = requests.get(query_url, headers = headers, params = params)
pprint(response.json())

