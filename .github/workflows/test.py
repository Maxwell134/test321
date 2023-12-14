from datetime import datetime
import os
from inputimeout import inputimeout, TimeoutOccurred

def find_employee(employee_id, employee):
    if employee in employee_id:
        current_time = datetime.now().strftime('%I:%M:%S %p')
        print('current_time:', current_time)
        print(f'Employee: {employee} exists in the list')
        return 'Found'
    return 'Not found'

def main():
    try:
        prompt = os.environ.get('PROMPT', '').lower()
        
        if prompt == 'yes':
            employee_id = ['001', '002', '003', '004', '005']
            employee_input = os.environ.get('employee', '')

            result = find_employee(employee_id, employee_input)
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
