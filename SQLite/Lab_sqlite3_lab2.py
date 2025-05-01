"""
Objectives
improving the student's skills in interacting with the SQLite database;
using known SQL statements.

Scenario
The application is almost ready. Let's add the missing functionalities to it:

Create a method called change_priority, responsible for updating task priority.
The method should get the id of the task from the user and its new priority (greater than or equal to 1).
Create a method called delete_task, responsible for deleting single tasks. The method should get the task id from the user.
Implement a simple menu consisting of the following options:

1. Show Tasks
2. Add Task
3. Change Priority
4. Delete Task
5. Exit
where:

Show Tasks (calls the show_tasks method)
Add Task (calls the add_task method)
Change Priority (calls the change_priority method)
Delete Task (calls the delete_task method)
Exit (interrupts program execution)
The program should obtain one of these options from the user, and then call the appropriate method of the TO_DO object.
Choosing option 5 must terminate the program.
A menu should be displayed in an infinite loop so that the user can choose an option multiple times.

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

    def change_priority(self):
        """
        The method should get the id of the task from the user and its new priority (greater than or equal to 1).
        """
        task_id = input('Enter id: ')
        new_priority = input('Enter new priority: ')
        if int(new_priority) >= 1:
            self.c.execute('UPDATE tasks SET priority = ? WHERE id = ?', (new_priority, task_id))
            self.conn.commit()

    def delete_task(self):
        """
        Create a method called delete_task, responsible for deleting single tasks.
        The method should get the task id from the user.
        """
        task_id = input('Enter id: ')
        self.c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()


if __name__ == "__main__":
    app = Todo()
    print('Options menu:\n'
          '1. Show Tasks\n'
          '2. Add Task\n'
          '3. Change Priority\n'
          '4. Delete Task\n'
          '5. Exit')
    choice = input('Enter selected option: ')
    if choice == '1':
        app.show_tasks()
    elif choice == '2':
        app.add_task()
    elif choice == '3':
        app.change_priority()
    elif choice == '4':
        app.delete_task()
    elif choice == '5':
        exit()
