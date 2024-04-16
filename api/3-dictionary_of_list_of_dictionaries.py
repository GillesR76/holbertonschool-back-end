#!/usr/bin/python3
"""Exporting all employees data into a json file"""
import json
import requests
import sys

if __name__ == '__main__':
    # Get all employees global info
    employees_url = "https://jsonplaceholder.typicode.com/users/"
    employees_response = requests.get(employees_url)
    employees = employees_response.json()

    tasks_dict = {}

    # Get all tasks of all employees
    for employee in employees:
        alltasks_url = ("https://jsonplaceholder.typicode.com/users/"
                        f"{employee['id']}/todos")
        alltasks_response = requests.get(alltasks_url)
        todos = alltasks_response.json()

        # Converting all the data into a dictionary
        all_tasks = []
        for task in todos:
            dict = {'username': employee['username'],
                    'task': task['title'], 'completed': task['completed']}
            all_tasks.append(dict)
        """
        Assigning into the dictionary all_tasks as values
        to each employee id as key
        """
        tasks_dict[employee['id']] = all_tasks

    # Converting the datas into a json file
    with open(f"todo_all_employees.json", 'w', encoding='utf8') as f:
        json_list = json.dump(tasks_dict, f)
