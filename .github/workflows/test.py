from datetime import datetime
import os

def employee_exists(employee_id, employee):
    if employee in employee_id:
        current_time = datetime.now().strftime('%I:%M:%S %p')
        print('current_time:', current_time)
        print(f'Employee: {employee} exists in the list')
        return 'Found'

    return 'Not found'

def main():
    employee = os.environ.get('employee')
    employee_id = ['001', '002', '003', '004', '005']
    result = employee_exists(employee_id, employee)
    print(result)

if __name__ == '__main__':
    main()
