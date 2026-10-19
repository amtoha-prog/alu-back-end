#!/usr/bin/python3
"""Export the TODO tasks of all employees to todo_all_employees.json."""
import json
import requests

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        all_tasks[str(user_id)] = [
            {"username": user.get("username"),
             "task": task.get("title"),
             "completed": task.get("completed")}
            for task in todos if task.get("userId") == user_id
        ]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)