#!/usr/bin/python3
"""Module"""

import requests
import json

"""Module"""

if __name__ == '__main__':
    # Construct the URL for todos information
    todos_url = "https://jsonplaceholder.typicode.com/todos/"

    # Send HTTP GET request to the URL and retrieve the JSON response
    todos_info = requests.get(todos_url).json()

    # Create a dictionary to store the tasks for each employee
    tasks_by_employee = {}

    # Iterate over each task and add it to the dictionary
    for task in todos_info:
        if task["userId"] not in tasks_by_employee:
            tasks_by_employee[task["userId"]] = []
        tasks_by_employee[task["userId"]].append(
            {
                "username": task["title"],
                "task": task["title"],
                "completed": task["completed"]
            }
        )

    # Write the dictionary to a JSON file
    with open("todo_all_employees.json", "w") as file:
        json.dump(tasks_by_employee, file)
