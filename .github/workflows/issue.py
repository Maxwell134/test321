import json
import os
import requests


token = os.getenv('GITHUB_TOKEN')
username = os.environ.get('username')
Repositoryname = os.environ.get('repo')
issue_number = os.environ.get('issue_number')

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
    print("::set-output name=comment_result::true")

else:
    print('sorry')
    print("::set-output name=comment_result::false")
