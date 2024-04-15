#!/usr/bin/python3

import requests
import sys
import csv

if __name__ == '__main__':
    int(sys.argv[1])
    # Get the employee's name
    employee_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{sys.argv[1]}")
    user_response = requests.get(employee_url)
    user_info = user_response.json()
    employee_name = user_info['name']

    # Get all the tasks of an employee
    alltasks_url = ("https://jsonplaceholder.typicode.com/users/"
                    f"{sys.argv[1]}/todos")
    alltasks_response = requests.get(alltasks_url)
    todos = alltasks_response.json()

    all_tasks = []
    for task in todos:
        list = [task['userId'], employee_name,
                task['completed'], task['title']]
        all_tasks.append(list)

    with open(f"{sys.argv[1]}.csv", 'w', encoding='utf8') as f:
        csv_list = csv.writer(f, quoting=csv.QUOTE_ALL)

        csv_list.writerows(all_tasks)
