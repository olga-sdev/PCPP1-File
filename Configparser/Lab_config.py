"""
Objectives
improving the student's skills in parsing configuration files;
improving the student's skills in creating configuration files.

Scenario
Imagine a situation in which you receive a configuration file containing access data for various services.
Unfortunately, the file is a terrible mess, because it contains data used in both production and development envs.

Your task will be to create two files named prod_config.ini and dev_config.ini.
The prod_config.ini file should only contain sections for the production environment,
while dev_config.ini should only contain sections for the development environment.

To distinguish between the environments, use the env option added to all sections in the mess.ini file.
The env option should be removed from the sections before moving them to the files.

Expected result
The prod_config.ini file:

[sentry]
key = key
secret = secret

[github]
user = user
password = password


The dev_config.ini file:

[mariadb]
host = localhost
name = hello
user = user
password = password

[redis]
host = localhost
port = 6379
db = 0

"""

import configparser

config = configparser.ConfigParser()
config.read('mess.ini')

with open('prod_config.ini', 'w') as config_prod_file:
    config.write(config_prod_file)

with open('dev_config.ini', 'w') as config_dev_file:
    config.write(config_dev_file)

config.read('prod_config.ini')

config.remove_section('mariadb')
config.remove_section('redis')

with open('prod_config.ini', 'w') as config_prod_file:
    config.write(config_prod_file)

config.read('dev_config.ini')

config.remove_section('sentry')
config.remove_section('github')

with open('dev_config.ini', 'w') as config_dev_file:
    config.write(config_dev_file)
