#### configparser module in Python

_configparser_ is a built-in module used for handling configuration files -> 
read, write, and modify structured _key-value pairs_ configuration files.

```
import configparser
```

The example of _config.ini_ file:

```
[Database]
host = localhost
port = 443
user = set-username
password = set-password
```

Read data from _config.ini_ with ConfigParser() method:

```
import configparser


config = configparser.ConfigParser()
print(config.read('config.ini'))

print('Sections:', config.sections())

print(config['Database']['host'])
print(config['Database']['port'])
print(config['Database']['user'])
print(config['Database']['password'])

"""
['config.ini']
Sections: ['Database']
localhost
443
set-username
set-password
"""
```

Reading data from dictionary with _config.read_dict()_ method:

```
import configparser


config = configparser.ConfigParser()

db_dict = {
    'Database': {
        'host': 'localhost',
        'port': 443,
        'user': 'set-username',
        'password': 'set-password'
    }
}

config.read_dict(db_dict)

print('Sections:', config.sections())

print(config['Database']['host'])
print(config['Database']['port'])
print(config['Database']['user'])
print(config['Database']['password'])

"""
Sections: ['Database']
localhost
443
set-username
set-password
"""
```

To create new config file .ini:

```
import configparser


config = configparser.ConfigParser()

config['Database'] = {'host': 'localhost',
                      'port': 443,
                      'user': 'set-username',
                      'password': 'set-password'}

with open('config_new.ini', 'w') as config_file:
    config.write(config_file)
```
