#!/usr/bin/python3
"""Fetch information about each employee toto list"""


import requests
import sys


if __name__ == '__main__':
    int(sys.argv[1])
    # Get the employee's name
    employee_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{sys.argv[1]}")
    user_response = requests.get(employee_url)
    user_info = user_response.json()
    employee_name = user_info.get('name')

    # Get all the tasks of an employee
    alltasks_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{sys.argv[1]}/todos")
    alltasks_response = requests.get(alltasks_url)
    todos = alltasks_response.json()

    # Count the total number of completed tasks and total tasks
    total_tasks = len(todos)
    count = 0
    for task in todos:
        if task.get('completed') is True:
            count += 1
    completed_tasks = count

    print(
        f"Employee {employee_name} is done with tasks"
        f"({completed_tasks}:{total_tasks}):")

    # Print the title of completed tasks
    for task in todos:
        if task.get('completed') is True:
            print(f"\t {task.get('title')}")
