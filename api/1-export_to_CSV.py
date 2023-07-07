#!/usr/bin/python3
"""
Module: employee_todo_report
This module retrieves information about an employee's TODO list from a REST API and generates a CSV report.
"""

import requests
import sys


if __name__ == '__main__':
    """IF SCRIPT IS NOT RUN AS MODULE"""

    # Retrieve the employee ID from the command-line argument
    employee_id = sys.argv[1]

    # Construct the URLs for user and todos information using the employee ID
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos/"

    # Send HTTP GET requests to the URLs and retrieve the JSON responses
    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    # Extract the employee's name and username from the user information
    employee_name = user_info["name"]
    employee_username = user_info["username"]

    # Filter the todos to get the completed tasks
    task_completed = list(filter(lambda obj: obj["completed"] is True, todos_info))

    # Calculate the number of completed tasks and total number of tasks
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    # Generate a CSV report with employee's ID, username, task completion status, and task title
    with open(f"{employee_id}.csv", "w") as file:
        for task in todos_info:
            file.write(f'"{employee_id}","{employee_username}","{task["completed"]}","{task["title"]}"
')
