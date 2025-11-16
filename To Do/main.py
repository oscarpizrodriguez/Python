import os

def add_task():
    task_title = input("Enter a title for the task: ")
    if not task_title:
        return
    else:
        if os.path.exists("tasks.txt"):
            file = open("tasks.txt", "a")
            file.write("[ ]" + task_title + "\n")
            file.close()
            print(task_title + " added\n")
        else:
            file = open("tasks.txt", "w")
            file.write("[ ]" + task_title + "\n")
            file.close()
    return

def delete_task():
    if not os.path.exists("tasks.txt"):
        return
    else:
        file = open("tasks.txt", "r")
        lines = file.readlines()
        for i, line in enumerate(lines, start=1):
            print(i, line.strip())
    option = input("Select task to delete > ")
    option = int(option)
    print("\n")
    if option < 1 or option > len(lines):
        return
    del lines[option - 1]
    file.close()
    file = open("tasks.txt", "w")
    file.writelines(lines)

def list_tasks():
    if not os.path.exists("tasks.txt"):
        return
    else:
        file = open("tasks.txt", "r")
        file = file.readlines()
        for line in file:
            print(line.strip())
        print("\n")

def complete_task():
    if not os.path.exists("tasks.txt"):
        return
    else:
        file = open("tasks.txt", "r")
        lines = file.readlines()
        file.close
        for i, line in enumerate(lines, start=1):
            print(i, line.strip())
        option = int(input("Select a task > "))
        lines[option - 1] = lines[option - 1].replace("[ ]", "[x]")
        file = open("tasks.txt", "w")
        file.writelines(lines)
        print("\n")

def main():
    while True:
        print("-- Main Menu --\n")
        print("1) Add task")
        print("2) Delete task")
        print("3) List tasks")
        print("4) Complete task")
        print("5) Exit\n")
        option = input("Select an option > ")
        if not option:
            pass
        elif option == "1":
            add_task()
        elif option == "2":
            delete_task()
        elif option == "3":
            list_tasks()
        elif option == "4":
            complete_task()
        elif option == "5":
            break
        else:
            pass

if __name__ == "__main__":
    main()