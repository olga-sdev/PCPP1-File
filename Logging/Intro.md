#### Logging in Python

Module _logging_ -> log events occurring in app, which helps to:
* find the cause of an error or possible problems;
* provide information for assuaring that everything works.

```
import logging
```

_getLogger_ is a function that create the logger for further work with logs (root logger).

```
logger = logging.getLogger()
```

*Logging levels*

| Level name  | Value | 
|-------------|-------|
| CRITICAL    | 50    | 
| ERROR       | 40    | 
| WARNING     | 30    | 
| INFO        | 20    | 
| DEBUG       | 10    |
| NOTSET      | 0     |	

```
logger.critical('CRITICAL log')
logger.error('ERROR log')
logger.warning('WARNING log')
logger.info('INFO log')
logger.debug('DEBUG log')
```

_setLevel()_ -> setting the log level causes messages with this or a higher level to be logged

```
import logging

logging.basicConfig()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.critical('CRITICAL log')
logger.error('ERROR log')
logger.warning('WARNING log')
logger.info('INFO log')
logger.debug('DEBUG log')

"""
CRITICAL:root:CRITICAL log
ERROR:root:ERROR log
WARNING:root:WARNING log
INFO:root:INFO log
"""
```

*Basic config*

Basic logging configuration with help of basicConfig() method. 
Calling the basicConfig method (without args) creates a StreamHandler object that processes the logs and then displays them in the console.
StreamHandler object is created by the default Formatter object responsible for the log format. 

_basicConfig()_ with three args:
* logging level -> only messages with this level will be processed;
* filename -> creates a FileHandler object (instead of a StreamHandler object) -> all logs will be directed to the specified file.
* filemode -> 'w' for overwrite, 'a' for append file.

```
import logging

logging.basicConfig(level=logging.ERROR, filename='prod.log', filemode='a')

logger = logging.getLogger()

logger.critical('CRITICAL log')
logger.error('ERROR log')
logger.warning('WARNING log')
logger.info('INFO log')
logger.debug('DEBUG log')

"""
prod.log file output:
CRITICAL:root:CRITICAL log
ERROR:root:ERROR log
"""
```

Additional resources https://docs.python.org/3/howto/logging.html
