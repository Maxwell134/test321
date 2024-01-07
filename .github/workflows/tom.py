import json
import os
import requests
from random import randint
import time

token = os.getenv('GITHUB_TOKEN')
username = os.environ.get('username')
Repositoryname = os.environ.get('repo')
issue_number = os.environ.get('issue_number')

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
response = requests.get(url, data = json.dumps(data),headers=headers)

if response.status_code == 200:
    issue_state = response.json().get('state', 'open')

    if issue_state == 'closed':
        # Step 2: Reopen the issue if it is closed
        reopen_url = f'https://api.github.com/repos/{username}/{Repositoryname}/issues/{issue_number}/comments'
        reopen_response = requests.patch(url, headers=headers, json={'state': 'open'})

        if reopen_response.status_code == 200:
            print(f"Issue reopened: https://github.com/{username}/{Repositoryname}/issues/{issue_number}")
        else:
            print(f"Failed to reopen issue. Status code: {reopen_response.status_code}")
    else:
        print(f"The issue is already open: https://github.com/{username}/{Repositoryname}/issues/{issue_number}")
else:
    print(f"Failed to retrieve issue information. Status code: {response.status_code}")

# print(f'https://github.com/{username}/{Repositoryname}/issues/{issue_number}')

# time.sleep(60)

# comment_url = f'https://api.github.com/repos/{username}/{Repositoryname}/issues/{issue_number}/comments'
# headers = {'Authorization': f'token {token}'}

# # Get comments on the issue
# comments = requests.get(comment_url, headers=headers)

# comment = any('yes' in comment['body']for comment in comments.json())

# print(comment)
# close_url = f'https://api.github.com/repos/{username}/{Repositoryname}/issues/{issue_number}'
# headers = {'Authorization': f'token {token}'}

# if comment:
#     response = requests.patch(close_url, headers=headers, json={'state': 'closed'})
#     print(response.json()['state'])

# else:
#     print('sorry')

