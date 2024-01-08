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


# Step3 :
# Delete exisitng comments if exist 

comments_url = f'https://api.github.com/repos/{username}/{Repositoryname}/issues/{issue_number}/comments'
comments_response = requests.get(comments_url, headers=headers)

if comments_response.status_code == 200:
    for comment in comments_response.json():
        comment_id = comment['id']
        delete_comment_url = f'https://api.github.com/repos/{username}/{Repositoryname}/issues/comments/{comment_id}'
        delete_comment_response = requests.delete(delete_comment_url, headers=headers)

        if delete_comment_response.status_code == 204:
            print(f"Deleted comment with ID {comment_id}")
        else:
            print(f"Failed to delete comment with ID {comment_id}. Status code: {delete_comment_response.status_code}")

# Step 4:
# Post your issue message using requests and json

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

