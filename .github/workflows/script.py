import os
import requests

def get_repository_interactions(owner, repo):
    url = f'https://api.github.com/repos/{owner}/{repo}/events'
    headers = {'Authorization': f'token {os.getenv("GITHUB_TOKEN")}'}
    response = requests.get(url, headers=headers)
    return response.json()

def main():
    owner = 'Maxwell134'
    repo = 'test321'

    interactions = get_repository_interactions(owner, repo)

    if interactions:
        for event in interactions:
            actor = event.get('actor', {}).get('login')
            if actor:
                print(f'GitHub user {actor} interacted with the repository.')

if __name__ == '__main__':
    main()
