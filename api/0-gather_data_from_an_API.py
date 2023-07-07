#!/usr/bin/python3
"""
Module: employee_todo_progress
This module retrieves and displays information about an employee's TODO list progress.
"""

import sys
import requests


def get_employee_info(employee_id):
    """
    Retrieves information about an employee from a JSON API.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        tuple: A tuple containing the employee's name, number of completed tasks,
               total number of tasks, and a list of completed task titles.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos/"

    user_info = requests.get(user_url).json()
    todos_info = requests.get(todos_url).json()

    employee_name = user_info.get("name")
    task_completed = [task.get("title") for task in todos_info if task.get("completed")]
    number_of_done_tasks = len(task_completed)
    total_number_of_tasks = len(todos_info)

    return employee_name, number_of_done_tasks, total_number_of_tasks, task_completed


def display_employee_progress(employee_id):
    """
    Displays the employee's TODO list progress.

    Args:
        employee_id (int): The ID of the employee.
    """
    employee_name, number_of_done_tasks, total_number_of_tasks, task_completed = get_employee_info(employee_id)

    print(f"Employee {employee_name} is done with tasks ({number_of_done_tasks}/{total_number_of_tasks}):")
    for task in task_completed:
        print(f"	{task}")


if __name__ == '__main__':
    """
    IF SCRIPT IS NOT RUN AS MODULE
    """
    if len(sys.argv) != 2:
        print("Usage: python3 employee_todo_progress.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_employee_progress(employee_id)
