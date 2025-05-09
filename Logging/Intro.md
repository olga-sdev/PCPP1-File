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

_Basic configuration_ refers to the initial setup of a logging system, which can include setting up handlers, formatters, and log levels. 
It provides a quick way to configure logging without needing to create handlers and formatters manually.

- Purpose: To quickly set up logging with minimal code.
- Configuration: Can include settings for log level, format, and output destinations (console, file, etc.).
- Simplicity: Ideal for simple applications or initial setup.

_basicConfig()_ with three args:
* logging level -> only messages with this level will be processed;
* filename -> creates a FileHandler object (instead of a StreamHandler object) -> all logs will be directed to the specified file;
* filemode -> 'w' for overwrite, 'a' for append file;
* format (by LogRecord object).

_format_ attributes:
* %(name)s – name of the logger that calls the logging method.
* %(levelname)s – set login level.
* %(asctime)s – human-readable date format with time when LogRecord object was created.
* %(message)s – defined message.

```
import logging


FORMAT = '%(name)s: %(levelname)s: %(asctime)s: %(message)s'
logging.basicConfig(level=logging.ERROR, filename='prod.log', filemode='a', format=FORMAT)

logger = logging.getLogger()

logger.critical('critical log')
logger.error('error log')
logger.warning('warning log')
logger.info('info log')
logger.debug('debug log')

"""
prod.log file output:

root: CRITICAL: 2025-05-09 12:15:33,064: critical log
root: ERROR: 2025-05-09 12:15:33,065: error log
"""
```

The FileHandler class, located in the core logging package, sends logging output to a disk file. 

_File handler_ is a component used in logging systems to direct log messages to a file. 
It manages the creation, writing, and rotation of log files. Here are some key points:

- Purpose: To write log messages to a file.
- Configuration: Typically involves specifying the file path, log format, and log level.
- Rotation: Can include settings for rotating log files based on size or time (e.g., daily, weekly).

```
import logging


FORMAT = '%(name)s: %(levelname)s: %(asctime)s: %(message)s'
logger = logging.getLogger()

handler = logging.FileHandler('prod_handler.log', mode='a')
logger.setLevel(logging.ERROR)

formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.critical('critical log')
logger.error('error log')
logger.warning('warning log')
logger.info('info log')
logger.debug('debug log')

"""
prod_handler.log file output:

root: CRITICAL: 2025-05-09 12:34:06,665: critical log
root: ERROR: 2025-05-09 12:34:06,666: error log
"""
```


Additional resources https://docs.python.org/3/howto/logging.html
