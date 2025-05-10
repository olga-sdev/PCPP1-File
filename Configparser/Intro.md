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
