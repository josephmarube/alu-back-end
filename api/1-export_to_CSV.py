#!/usr/bin/python3
"""Export employee TODO list data to CSV format."""
import csv
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
    filename = "{}.csv".format(employee_id)

    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task.get("completed"),
                task.get("title")
            ])