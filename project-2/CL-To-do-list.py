from pathlib import Path
import json
from operator import indexOf


task_data = {}
task_titles = {}
task_statuses = {}
task_priorities = {}
task_due_dates = {}
task_ids = {}
glob = {}

class Task:
    def __init__(self, title, status, priority, due_date,theid):
        self.title = title
        self.status = status
        self.priority = priority
        self.due_date = due_date
        self._id = theid
    # def __str__(self):
    #     return f"{self.title} - {self.status} - {self.priority} - {self.due_date}"
    def delete(self):
        del task_data[self.id]
        del task_titles[self.id]
        del task_statuses[self.id]
        del task_priorities[self.id]
        del task_due_dates[self.id]
        del task_ids[self.id]


def update(my_dict :dict)->dict:
    my_dict["task_data"] = task_data
    my_dict["task_titles"] = task_titles
    my_dict["task_statuses"] = task_statuses
    my_dict["task_priorities"] = task_priorities
    my_dict["task_due_dates"] = task_due_dates
    my_dict["task_ids"] = task_ids
    return my_dict
def displayMenu1():
    print("1. AddTaskList")
    print("2. EmptyTaskList")
    print("3. ModifyTaskList")
    print("4. CompleteTaskList")
    print("5. DisplayTaskList")
    print("4. Exit")

def displayMenu2():
    print("1. AddTask")
    print("2. RemoveTask")
    print("3. ModifyTask")
    print("4. CompleteTask")
    print("5. DisplayTask")
    print("6. Exit")

path = Path.cwd()/'tasks.json'
with open(path, "r+") as file:
    data = json.load(file)
    data = data["task_data"]

    task_data = {data: valeur for data, valeur in data.items() if data not in task_data}
    # task_titles = {data: valeur for data, valeur in data.items() if data not in task_titles}
    # task_statuses = {data: valeur for data, valeur in data.items() if data not in task_statuses}
    # task_priorities = {data: valeur for data, valeur in data.items() if data not in task_priorities}
    # task_due_dates = {data: valeur for data, valeur in data.items() if data not in task_due_dates}
    # task_ids = {data: valeur for data, valeur in data.items() if data not in task_ids}
while True:
        displayMenu1()
        choice = input("Enter your choice: ")
        if choice == "1":
            # Add a tasklist
            try:
                title = input("Enter the tasklist title: ")
                print("Tasklist added successfully")
            except ValueError:
                print("Sorry, Something went wrong")
            task_data.update({title: {"id": len(task_data)}})
            update(glob)
            print(task_data)
            print(glob)
            with open(path, "w") as file:
                json.dump(glob, file)
        elif choice == "2":
            # Empty a tasklist
            try:
                title = input("Enter the tasklist title: ")
            except ValueError:
                print("Sorry, Something went wrong")
            task_data.pop(title)
            print(task_data)
            update(glob)
            with open(path, "w") as file:
                json.dump(glob, file)
        elif choice == "3":
            displayMenu2()
            choice = input("Enter your choice: ")
        elif choice == "5":
            # Display a tasklist
            try:
                title = input("Enter the tasklist title: ")
                print(task_data[title])
            except ValueError:
                print("Sorry, Something went wrong")
        # elif choice == "2":
        #     # Empty a tasklist
        #     try:
        #         title = input("Enter the tasklist title: ")
        #         print("Tasklist emptied sccessfully")
        #     except ValueError:
        #         print("Sorrt, Something went wrong")