#!/usr/bin/python3
"""Exporting an employee's data into a csv file"""


import csv
import requests
import sys


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    # Get the employee's name
    employee_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{employee_id}")
    user_response = requests.get(employee_url)
    user_info = user_response.json()
    EMPLOYEE_NAME = user_info.get('username')

    # Get all the tasks of an employee
    alltasks_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{employee_id}/todos")
    alltasks_response = requests.get(alltasks_url)
    todos = alltasks_response.json()

    all_tasks = []
    for task in todos:
        list = [task.get('userId'), EMPLOYEE_NAME,
                task.get('completed'), task.get('title')]
        all_tasks.append(list)

    with open(f"{employee_id}.csv", 'w', encoding='utf8') as f:
        csv_list = csv.writer(f, quoting=csv.QUOTE_ALL)

        csv_list.writerows(all_tasks)
