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
