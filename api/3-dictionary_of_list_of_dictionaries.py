#!/usr/bin/python3
"""
Exports TODO list of all employees to JSON format.
"""

import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    users = users_response.json()
    todos = todos_response.json()

    data = {}

    for user in users:
        user_id = str(user.get("id"))
        username = user.get("username")

        user_tasks = []

        for task in todos:
            if task.get("userId") == user.get("id"):
                user_tasks.append({
                    "username": username,
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })

        data[user_id] = user_tasks

    with open("todo_all_employees.json", mode="w") as json_file:
        json.dump(data, json_file)