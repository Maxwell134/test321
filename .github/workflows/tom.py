import json
import os
import requests

token = os.getenv('GITHUB_TOKEN')
username = os.environ.get('username')
Repositoryname = os.environ.get('repo')

"""
Step 1:
Create contents for the issue you want to post
"""
headers = {"Authorization": f"token {token}"}
data = {
    "title": "Found a bug",
    "body": 'Prompt for yes or no : \n\n  - [ ] yes  \n - [ ] no'
}

"""
Step 2:
Generate your target repository's URL using Github API
"""
url = f"https://api.github.com/repos/{username}/{Repositoryname}/issues"

"""
Step 3:
Post your issue message using requests and json
"""
response = requests.post(url, data=json.dumps(data), headers=headers)

if response.status_code == 201:
    print(f"New issue created: {response.json()['html_url']}")
else:
    print(f"Failed to create issue. Status code: {response.status_code}")
    print(response.text)
