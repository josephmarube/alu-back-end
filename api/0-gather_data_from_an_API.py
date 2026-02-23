#!/usr/bin/python3
"""
Fetches and displays TODO list progress of a given employee
using JSONPlaceholder REST API.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url,
                                  params={"userId": employee_id})

    user = user_response.json()
    todos = todos_response.json()

    employee_name = user.get("name")
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))