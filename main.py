from datetime import date
import json

def list_tasks():
    task_list = load_tasks()
    for items in task_list:
        print(items)

def complete_task():
    id = int(input("Enter your id for the task"))
    task_list = load_tasks()
    flag = 0
    for i in range(len(task_list)):
        if task_list[i]["ID"]==id:
            task_list[i]["Status"]="Complete"
            flag = 1
            save_tasks(task_list)
            break
    if flag ==0:
        print("ID doesnt exists")
            
    

def delete_task():
    id = int(input("Enter your id for the task"))
    task_list = load_tasks()
    flag = 0
    for i in range(len(task_list)):
        if task_list[i]["ID"]==id:
            task = task_list[i]
            flag = 1
            break
    if flag ==0:
        print("ID doesnt exists")
    else:
        task_list.remove(task)
        save_tasks(task_list)


def load_tasks():
    filename = "tasks.json"
    try:
        with open(filename, "r") as f:
            return json.load(f)
        

    except FileNotFoundError:
            return []

def save_tasks(task_list):
    with open("tasks.json", "w") as f:
        json.dump(task_list, f)

def add_task():
    title = input("Please add a task:")
    status = "Pending"
    created_Date = date.today()
    created_Date = created_Date.strftime("%Y-%m-%d")
    task_list = load_tasks()
    if len(task_list)==0:
        id = 1
    else:
        id = max(item['ID'] for item in task_list) + 1

    task = {"ID":id, "Title": title, "Status": status, "Date": str(created_Date)}

    task_list.append(task)
    # print(task_list)
    save_tasks(task_list)

        
        



while True:
    print("Choose an option:")
    print("1) Add a Task")
    print("2) View all Task")
    print("3) Edit a Task")
    print("4) Delete a Task")
    print("5) EXIT")
    
    val  = int(input())

    if val == 1:
        add_task()
    elif val == 2:
        list_tasks()
    elif val == 3:
        complete_task()
    elif val == 4:
        delete_task()    
    else:
        break
        

