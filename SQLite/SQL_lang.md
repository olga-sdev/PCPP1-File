SQL is a _Structured Query Language_ for creating, modifying, and managing relational databases https://www.sqlite.org/lang.html

To _Create table_ with datatype https://www.sqlite.org/datatype3.html:

```
CREATE TABLE table_name (
…
columnN datatype
);
```

Example of table creation:
```
import sqlite3

# Connection object is created
conn = sqlite3.connect('sql_new_db.db')

# Cursor object -> allows any SQL statements to be executed in the DB
c = conn.cursor()

# Executes the CREATE TABLE statement in DB if it was created before
c.execute('''CREATE TABLE IF NOT EXISTS job_application (
id INTEGER PRIMARY KEY,
full_name TEXT NOT NULL,
email TEXT NOT NULL,
summary TEXT NOT NULL
);''')
```

_Inserting data into Table_ with _INSERT INTO_ statement using named parameters for security reason:

* first option:

```
data = {"id": 1,
        "full_name": "First_name Last_name",
        "email": "info@job.com",
        "summary": "Description about job experience and skills"}

c.execute("INSERT INTO job_application (id, full_name, email, summary)"
          "VALUES (:id, :full_name, :email, :summary)", data)
```

* second option:

```
c.execute("INSERT INTO job_application"
          "VALUES (:id, :full_name, :email, :summary)", data)
```

Confirm changes of trusaction:
```
conn.commit()
```

Close connection with DB:
```
conn.close()
```
