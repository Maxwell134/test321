import os
import json
import requests

# Personal access token for authentication
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

# The repository to add this issue to
REPO_OWNER = 'Maxwell134'
REPO_NAME = 'test321'

def make_github_issue(title, body=None, labels=None):
    '''Create an issue on github.com using the given parameters.'''
    # Our url to create issues via POST
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues'
    # Create an authenticated session to create the issue
    session = requests.Session()
    session.headers = {'Authorization': f'Bearer {GITHUB_TOKEN}',
                       'Accept': 'application/vnd.github.v3+json'}
    # Create our issue
    issue = {'title': title,
             'body': body,
             'labels': labels}
    # Add the issue to our repository
    r = session.post(url, json=issue)
    if r.status_code == 201:
        print('Successfully created Issue {0:s}'.format(title))
    else:
        print('Could not create Issue {0:s}'.format(title))
        print('Response:', r.content)

# Example usage
make_github_issue('Test Issue', 'This is a test issue created using a token.')
