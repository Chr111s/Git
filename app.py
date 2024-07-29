
# app.py
tasks = []

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

if __name__ == "__main__":
    print("Welcome to GitTutorialApp")
    add_task("Finish Git tutorial")
    print("Current tasks:", tasks)
