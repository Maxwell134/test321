import os
import requests

def get_collaborators(repo_owner, repo_name, github_token):
    collaborators_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/collaborators'
    headers = {'Authorization': f'token {github_token}'}
    
    response = requests.get(collaborators_url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad responses
    
    collaborators = response.json()
    return [collaborator['login'] for collaborator in collaborators]

def main():
    repo_owner = 'Maxwell134'
    repo_name = 'test321'
    github_token = os.getenv('GITHUB_TOKEN')
    
    if not github_token:
        print('GitHub token not found.')
        return
    
    try:
        collaborators = get_collaborators(repo_owner, repo_name, github_token)
        if collaborators:
            print('GitHub collaborators:')
            for collaborator in collaborators:
                print('-', collaborator)
        else:
            print('No collaborators found for the repository.')
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
