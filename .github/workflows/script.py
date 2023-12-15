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

    actors_set = set()

    if interactions:
        for event in interactions:
            actor = event.get('actor', {}).get('login')
            if actor:
                actors_set.add(actor)

    actors_list = list(actors_set)

    if actors_list:
        print(f'GitHub actors associated with the repository: {", ".join(actors_list)}')
    else:
        print('No GitHub actors found for the repository.')

if __name__ == '__main__':
    main()
