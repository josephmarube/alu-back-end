#!/usr/bin/python3
"""
Exports TODO list of a given employee to CSV format.
"""

import csv
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

    filename = "{}.csv".format(employee_id)

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])