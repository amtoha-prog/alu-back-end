#!/usr/bin/python3
"""Returns TODO list progress for a given employee ID using a REST API."""
import requests
import sys

if __name__ == "__main__":
    base = "https://jsonplaceholder.typicode.com"
    emp_id = sys.argv[1]

    user = requests.get("{}/users/{}".format(base, emp_id)).json()
    todos = requests.get("{}/todos".format(base),
                         params={"userId": emp_id}).json()

    done = [t for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for t in done:
        print("\t {}".format(t.get("title")))
