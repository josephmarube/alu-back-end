#!/usr/bin/python3
"""Export employee TODO list data to JSON format."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": employee_id}
    ).json()

    username = user.get("username")
    filename = "{}.json".format(employee_id)

    tasks = [
        {
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        }
        for t in todos
    ]

    with open(filename, mode="w") as f:
        json.dump({employee_id: tasks}, f)