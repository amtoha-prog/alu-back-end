#!/usr/bin/python3
"""Export all TODO tasks of an employee to a JSON file named USER_ID.json."""
import json
import requests
import sys

if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": employee_id}).json()
    username = user.get("username")

    tasks = [{"task": task.get("title"),
              "completed": task.get("completed"),
              "username": username} for task in todos]

    with open("{}.json".format(employee_id), "w") as json_file:
        json.dump({employee_id: tasks}, json_file)