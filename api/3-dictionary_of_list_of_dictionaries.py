#!/usr/bin/python3
"""Exports all employees' TODO data to a JSON file."""
import json
import requests

if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base)).json()
    todos = requests.get("{}/todos".format(base)).json()

    data = {}
    for user in users:
        data[str(user["id"])] = [
            {"username": user["username"],
             "task": t["title"],
             "completed": t["completed"]}
            for t in todos if t["userId"] == user["id"]
        ]

    with open("todo_all_employees.json", "w") as f:
        json.dump(data, f)
