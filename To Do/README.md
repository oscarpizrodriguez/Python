
# ToDo

This project is a simple console-based task management application developed in Python. It allows users to add, list, complete, and delete tasks through an interactive menu. Tasks are stored in a text file (tasks.txt), ensuring data persistence between program runs.

The main goal of this script is to provide a lightweight and functional solution for basic task handling without the need for databases or graphical interfaces. Its modular structure makes the code easy to read, maintain, and extend.




## Tech Stack

**Python 3** – Core programming language used to build the application.

**OS Module** – Used for file and path management (checking if tasks.txt exists, creating and updating files).

**File I/O (Input/Output)** – Handles reading from and writing to the task storage file.

**Command-Line Interface (CLI)** – Provides an interactive text-based user experience.
## Deployment

1. Clone this repository

```bash
git clone https://github.com/your-username/task-manager.git
cd task-manager
```

2. Ensure python is installed

```bash
python --version
```

3. Run the application
```bash
python main.py
```

4. Using the program
Once launched, the main menu will appear, allowing you to:

- Add new tasks

- List all tasks

- Mark tasks as completed

- Delete tasks

- Exit the program

No additional dependencies or configuration are required. The application automatically creates a `tasks.txt` file in the project directory to store your tasks.
