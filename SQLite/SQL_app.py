import sqlite3


class Application:
    def __init__(self):
        self.conn = sqlite3.connect('job_app.db')
        self.c = self.conn.cursor()
        self.create_job_app_table()

    def create_job_app_table(self):
        self.c.execute('''CREATE TABLE IF NOT EXISTS job_application (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        full_name TEXT NOT NULL,
                        email TEXT NOT NULL,
                        summary TEXT NOT NULL
                        );''')

    def add_job_app(self):
        name = input('Enter full name: ')
        email = input('Enter email: ')
        summary = input('Enter brief summary: ')

        data = {"full_name": name,
                "email": email,
                "summary": summary}

        self.c.execute("INSERT INTO job_application (full_name, email, summary)"
                       "VALUES (:full_name, :email, :summary)", data)
        self.conn.commit()
        self.conn.close()

    def read_job_app(self):
        name = input('Enter name of candidate: ')
        self.c.execute(f'SELECT * FROM job_application WHERE full_name = "{name}"')
        row = self.c.fetchone()
        print(row)
        self.conn.close()

    def read_all_data(self):
        self.c.execute('SELECT * FROM job_application')
        rows = self.c.fetchall()
        for row in rows:
            print(row)
        self.conn.close()


if __name__ == "__main__":
    app = Application()
    choice = input('Manipulation with DB: 1-add new data; 2-read data by name; 3-read all data.\n Select option: ')
    if choice == '1':
        app.add_job_app()
    elif choice == '2':
        app.read_job_app()
    elif choice == '3':
        app.read_all_data()


"""
Manipulation with DB: 1-add new data; 2-read data by name; 3-read all data.
 Select option: 3
(1, 'John Doe', 'john@mail.com', 'Python developer with 10 years of experience: Flask, Django, FastAPI, Tkinter, Kivy')
(2, 'Anna Smith', 'anna@mail.com', 'QA Engineer: manual and automation testing with Python')
(3, 'Viktor Micle', 'viktor@mail.com', 'DevOps: AWS, GCP, Aure, CICD, Jenkins')
(4, 'Adam', 'adam@mail.com', 'Scrum Master')
(5, 'George', 'ge@mail.com', 'PO')

Manipulation with DB: 1-add new data; 2-read data by name; 3-read all data.
 Select option: 1
Enter full name: Dan
Enter email: dan@mail.com
Enter brief summary: PM

Manipulation with DB: 1-add new data; 2-read data by name; 3-read all data.
 Select option: 2
Enter name of candidate: Dan
(6, 'Dan', 'dan@mail.com', 'PM')
"""
