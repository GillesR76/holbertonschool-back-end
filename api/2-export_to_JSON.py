#!/usr/bin/python3
"""Exporting an employee's data into a json file"""


import requests
import sys
import json


if __name__ == '__main__':
    int(sys.argv[1])
    # Get the employee's name
    employee_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{sys.argv[1]}")
    # Converts the response from the server into a Python dictionary
    user_response = requests.get(employee_url)
    user_info = user_response.json()
    employee_name = user_info['name']

    # Get all the tasks of an employee
    alltasks_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{sys.argv[1]}/todos")
    alltasks_response = requests.get(alltasks_url)
    todos = alltasks_response.json()

    # Converting the data into a dictionary
    all_tasks = []
    for task in todos:
        dict = {'task': task['title'], 'completed': task['completed'],
                'username': employee_name}
        all_tasks.append(dict)
    tasks_dict = {task['userId']: all_tasks}

    # Converting the data into a json file
    with open(f"{sys.argv[1]}.json", 'w', encoding='utf8') as f:
        json_list = json.dump(tasks_dict, f)
