#!/usr/bin/python3
""" using this REST API - https://jsonplaceholder.typicode.com,
    for a given employee ID,
    returns information about his/her TODO list progress.

Usage: ./0-gather_data_from_an_API.py 2
"""
import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        user_id = int(sys.argv[1])
        users_url = "https://jsonplaceholder.typicode.com/users?userId={}".format(user_id)
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
        users = requests.get(users_url).json()
        todos = requests.get(todos_url)
        todos = todos.json()


        completed_tasks = []
        for todo in todos:
            if(todo["completed"]):
                completed_tasks.append(todo["title"])

        total_tasks = len(todos)
        completed_count = len(completed_tasks)
        
        print("Employee {} is done with tasks({}/{})".format(users[user_id]["name"], completed_count, total_tasks))
        for title in completed_tasks:
            print("\t {}".format(title))

    else:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")

