# app.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' deleted.")
    else:
        print(f"Task '{task}' not found.")

if __name__ == "__main__":
    print("Welcome to GitTutorialApp")
    add_task("Finish Git tutorial")
    delete_task("Finish Git tutorial")
    print("Current tasks:", tasks)
