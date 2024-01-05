import requests
import os
import time
import json

# Replace these variables with your GitHub credentials and repository information
github_token = os.environ.get('GITHUB_TOKEN')
repo_owner = "OWNER"
repo_name = "REPO_NAME"
pr_number = os.environ.get('GITHUB_EVENT_PATH')  # Use GitHub event payload to get PR number
pr_number = json.load(open(pr_number))['number']

# Create approval issue
issue_data = {
    "title": "Approval Required",
    "body": "Please approve or deny this pull request.",
    "labels": ["approval"]
}

headers = {
    "Authorization": f"Bearer {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

response = requests.post(
    f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues",
    json=issue_data,
    headers=headers
)

if response.status_code == 201:
    print("Approval issue created successfully.")
    issue_number = response.json()["number"]
else:
    print(f"Failed to create approval issue. Status code: {response.status_code}")
    exit(1)

# Check approval status
while True:
    response = requests.get(
        f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}",
        headers=headers
    )
    if response.status_code != 200:
        print(f"Failed to fetch issue details. Status code: {response.status_code}")
        exit(1)

    issue_state = response.json()["state"]

    if issue_state == "closed":
        print("Approval denied. Exiting the script.")
        exit(1)
    elif issue_state == "open":
        print("Approval pending. Waiting for approval...")
        time.sleep(60)  # Wait for 1 minute before checking again
    else:
        print(f"Unexpected approval status: {issue_state}. Exiting the script.")
        exit(1)

# Proceed to the next step
print("Approval received. Proceeding to the next step.")
# Add your code for the next step here
