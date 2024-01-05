import os
from github import Github

# Replace 'YOUR-TOKEN' with your GitHub personal access token
token = ''
repo_owner = "Maxwell134"
repo_name = "test321"

# Create a GitHub instance using the token
g = Github(token)

# Get the repository
repo = g.get_repo(f"{repo_owner}/{repo_name}")

# Create an issue
issue_title = "Found a bug"
issue_body = "I'm having a problem with this."
assignees = ["octocat"]
labels = ["bug"]

# Create the issue without the milestone parameter
issue = repo.create_issue(title=issue_title, body=issue_body, assignees=assignees, labels=labels)

print(f"Issue created successfully! Issue Number: {issue.number}")
