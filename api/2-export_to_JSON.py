#!/usr/bin/python3
"""
Exports TODO list of a given employee to JSON format.
"""

import json
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

    username = user.get("username")

    tasks_list = []

    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    data = {employee_id: tasks_list}

    filename = "{}.json".format(employee_id)

    with open(filename, mode="w") as json_file:
        json.dump(data, json_file)