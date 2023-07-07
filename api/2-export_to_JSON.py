#!/usr/bin/python3
""" Module"""

import requests
import sys

""" Documented"""

if __name__ == "__main__":
    """ Get employee ID from command line argument """
    employee_id = sys.argv[1]

    # Get user and todos URLs
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos/".format(
        employee_id
    )

    # Get user and todos information from URLs
    user_info = requests.request("GET", user_url).json()
    todos_info = requests.request("GET", todos_url).json()

    # Extract employee name and username from user information
    employee_name = user_info["name"]
    employee_username = user_info["username"]

    # Filter completed tasks and get number of done tasks
    task_completed = list(filter(lambda obj: (obj["completed"] is True), todos_info))
    number_of_done_tasks = len(task_completed)

    # Get total number of tasks
    total_number_of_tasks = len(todos_info)

    # Write employee ID, username, task completion status and title to CSV file
    with open(str(employee_id) + ".csv", "w") as file:
        [
            file.write(
                '"'
                + str(employee_id)
                + '",'
                + '"'
                + employee_username
                + '",'
                + '"'
                + str(task["completed"])
                + '",'
                + '"'
                + task["title"]
                + '",'
                + "
"
            )
            for task in todos_info
        ]
