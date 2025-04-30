"""
Objectives
improving the student's skills in interacting with the SQLite database;
using known methods of the Cursor object.
Scenario
Our to_do application requires you to add a little security and display the data saved in the database. Your task is to implement the following functionalities:

Create a find_task method, which takes the task name as its argument. The method should return the record found or None otherwise.
Block the ability to enter an empty task (the name cannot be an empty string).
Block the ability to enter a task priority less than 1.
Use the find_task method to block the ability to enter a task with the same name.
Create a method called show_tasks, responsible for displaying all tasks saved in the database.
Test data:

Example input:
Enter task name: My first task
Enter priority: 1

Example output:
(1, 'My first task', 1)

Example input:
Enter task name: My second task
Enter priority: 2

Example output:
(1, 'My first task', 1)
(2, 'My second task', 2)

Example input:
Enter task name: My first task
Enter priority: 1

Example output:
(1, 'My first task', 1)
(2, 'My second task', 2)
"""

import sqlite3


class Todo:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.c = self.conn.cursor()
        self.create_task_table()

    def create_task_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS tasks (
                     id INTEGER PRIMARY KEY,
                     name TEXT NOT NULL,
                     priority INTEGER NOT NULL
                     );''')

    def add_task(self):
        """
        Block the ability to enter an empty task (the name cannot be an empty string).
        Block the ability to enter a task priority less than 1.
        Use the find_task method to block the ability to enter a task with the same name.
        """
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))

        if name is not None and app.find_task(name) is None and priority >=1:
            self.c.execute('INSERT INTO tasks (name, priority) VALUES (?,?)', (name, priority))
            self.conn.commit()

    def find_task(self, name):
        """
        Create a find_task method, which takes the task name as its argument.
        The method should return the record found or None otherwise
        """
        self.c.execute(f'SELECT * FROM tasks WHERE name = "{name}"')
        row = self.c.fetchone()
        return row

    def show_tasks(self):
        """
        Create a method called show_tasks, responsible for displaying all tasks saved in the database.
        """
        self.c.execute('SELECT * FROM tasks')
        rows = self.c.fetchall()
        for row in rows:
            print(row)


app = Todo()
app.add_task()
app.show_tasks()
