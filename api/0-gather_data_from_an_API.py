#!/usr/bin/python3
"""Module"""

import requests
import sys

"""Module"""

if __name__ == '__main__':
    """IF SCRIPT IS NOT RUN AS MODULE"""
    # Retrieve the employee ID from the command-line argument
    employee_id = sys.argv[1]
    # Construct the URLs for user and todos information using the employee ID
    user_url = "https://jsonplaceholder.typicode.com/users/{}" \
        .format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/" \
        .format(employee_id)

    # Send HTTP GET requests to the URLs and retrieve the JSON responses
    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

     # Extract the employee's name from the user information
    employee_name = user_info["name"]
    # Filter the todos to get the completed tasks
    task_completed = list(filter(lambda obj:
                                 (obj["completed"] is True), todos_info))
    # Calculate the number of completed tasks and total number of tasks
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    # Print the employee's name and task progress
    print("Employee {} is done with tasks({}/{}):".
          format(employee_name, number_of_done_tasks, total_number_of_tasks))

    # Print the titles of completed tasks
    [print("	 " + task["title"]) for task in task_completed]
