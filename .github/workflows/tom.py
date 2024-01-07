import json
import os
import requests
from random import randint

token = os.getenv('GITHUB_TOKEN')
username = os.environ.get('username')
Repositoryname = os.environ.get('repo')
issue_number = randint(1,20)

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
url = f"https://api.github.com/repos/{username}/{Repositoryname}/issues/{issue_number}"

"""
Step 3:
Post your issue message using requests and json
"""
requests.post(url, data=json.dumps(data), headers=headers)

issue = f'https://github.com/{username}/{Repositoryname}/issues/{issue_number}'
os.popen(f'echo {issue}')

time.sleep(180)

comment_url = f'https://api.github.com/repos/{username}/{Repositoryname}/issues/{issue_number}/comments'
headers = {'Authorization': f'token {token}'}

# Get comments on the issue
comments = requests.get(comment_url, headers=headers)

comment = any('yes' in comment['body']for comment in comments.json())

print(comment)
close_url = f'https://api.github.com/repos/{username}/{Repositoryname}/issues/{issue_number}'
headers = {'Authorization': f'token {token}'}

if comment:
    response = requests.patch(close_url, headers=headers, json={'state': 'closed'})
    print(response.json()['state'])

else:
    print('sorry')

