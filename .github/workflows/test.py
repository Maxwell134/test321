from datetime import datetime
import os
import requests
from inputimeout import inputimeout, TimeoutOccurred
from time import sleep  # Import the sleep function

def get_github_actors(repo_owner, repo_name, github_token):
    collaborators_url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/collaborators'
    headers = {'Authorization': f'token {github_token}'}
    
    response = requests.get(collaborators_url, headers=headers)
    response.raise_for_status()  # Raise an exception for bad responses
    
    collaborators = response.json()
    return [collaborator['login'] for collaborator in collaborators]

def find_employee(employee_id, github_actors, employee):
    if employee in employee_id:
        current_time = datetime.now().strftime('%I:%M:%S %p')
        print('current_time:', current_time)
        print(f'Employee: {employee} exists in the list')

        if employee in github_actors:
            print(f'Employee {employee} is also a GitHub actor.')
            return 'Found'
        else:
            print(f'Employee {employee} is not a GitHub actor.')
            return 'Not found'
    
    return 'Not found'

def main():
    try:
        for i in range(10):  # Use a for loop for a finite number of iterations
            prompt = os.environ.get('PROMPT', '').lower()
            sleep(1)

        if prompt == 'yes':
            repo_owner = 'your-username'
            repo_name = 'your-repo-name'
            github_token = os.getenv('GITHUB_TOKEN')
            
            if not github_token:
                print('GitHub token not found.')
                return
            
            github_actors = get_github_actors(repo_owner, repo_name, github_token)

            employee_id = ['001', '002', '003', '004', '005', 'Maxwell134']
            employee_input = os.environ.get('employee', '')

            result = find_employee(employee_id, github_actors, employee_input)
            print(result)
            print(f"::set-output name=result::{result}")

        elif prompt == 'no':
            print('Exiting')
        else:
            print('Invalid input.')
    except Exception as e:
        print(f'Error: {str(e)}')

if __name__ == '__main__':
    main()
