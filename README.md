# logger

## Description

A module that allows you to log messages to a file, console, logstash and redis pubsub.

By default, only console logging is enabled.

In order to enable logging in the redis pubsub, logstash, file after initializing the logger object, you must call methods with output parameters.

To log in redis pubsub, you must additionally install the redis library.

## Example of work:
```python
from log.app import Logger

logger = Logger(service_name='test-service', log_level='debug')
logger.log_to_file(filename='test-service.log')
logger.log_to_logstash(host='LOGSTASH_HOST', port=6004, logstash_network='udp')
logger.log_to_redis(host='REDIS_LOG_HOST', port='REDIS_LOG_PORT', topic='REDIS_PUBSUB_TOPIC')


logger.info('Info message')
logger.error('Error message')

logger.metric('Metric message', query_time=100, queue_size=200)
```

## Recommendations

It is recommended to initialize the logger object once in the entire project, and then import the object itself.

## Installation and update options

```
To use the project, you need to register an ssh key in the system and git.

Module update: pip install --upgrade git+ssh://git@gitadress.com/qa/logger.git

To install (update) a module from a specific branch: pip install (--upgrade) git+ssh://git@gitadress.com/qa/logger.git@branch_name

To install a specific package use eggs: pip install git+ssh://git@gitadress.com/qa/logger.git@branch_name#egg=logger

```