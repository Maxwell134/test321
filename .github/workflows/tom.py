
import requests
import json
import os

token = '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'
username = 'Maxwell134'
Repositoryname = 'test321'
number = 16
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

url = "https://api.github.com/repos/{}/{}/issues/{}".format(username,Repositoryname, number)

"""
Step 3:
Post your issue message using requests and json
"""
response = requests.post(url,data=json.dumps(data),headers=headers)

print(response.text)

print(f'https://api.github.com/repos/{username}/{Repositoryname}/issues/{number}')


