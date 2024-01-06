import requests
import json
import os

token = os.getenv('GITHUB_TOKEN')
username = os.getenv('username')
Repositoryname = os.getenv('Repositoryname')

"""
Step 1:
Create contents for the issue you want to post
"""
headers = {"Authorization" : "token {}".format(token)}
data = {"title": "Found a bug",
        "body" : 'Prompt for yes or no : \n\n  - [ ] yes  \n - [ ] no'

        }

"""
Step 2:
Generate your target repository's URL using Github API
# """

url = "https://api.github.com/repos/{}/{}/issues".format(username,Repositoryname)

"""
Step 3:
Post your issue message using requests and json
"""
requests.post(url,data=json.dumps(data),headers=headers)
print(f'https://github.com/{username}/{Repositoryname}/issues')


