The _database management system (DBMS)_ is the software responsible for:

* creating a database structure;
* inserting, updating, deleting, and retrieving data;
* ensuring data security;
* transaction management;
* ensuring concurrent access to data for many users;
* enabling data exchange with other database systems.

_SQLite DB_ is stored in one file. 
SQLite doesn't require a separate server process to be running in order to communicate with the DB.
SQLite doesn't require configuration, because it's a self-contained library enclosed in one source file.

The standard Python library has a module called sqlite3, providing an interface compliant with the DB-API 2.0 specification described by _PEP 249_: https://peps.python.org/pep-0249/. 
The purpose of the DB-API 2.0 specification is to define a _common standard for creating modules_ to work with databases in Python.

![image](https://github.com/user-attachments/assets/1e08a102-f459-4cda-b2d9-9dc38c8d9583)

To use the sqlite3 module - import it:

```
import sqlite3
```

