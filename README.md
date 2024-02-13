# logger

## Описание

Модуль позволяющий логгировать сообщения в файл, консоль, logstash и redis pubsub.

По умолчанию включено только логгирование в консоль.

Для того, чтобы включить логгирование в redis pubsub, logstash, файл после инициализации объекта логгера необходимо вызвать методы с параметрами вывода.

Для логирования в redis pubsub, необходимо дополнительно установить библиотеку redis.

## Пример работы:
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

## Рекомендации

Рекомендуется инициализировать объект логгера один раз во всём проекте, и далее импортировать сам объект.

## Варианты установки и обновления

```
Для использования проекта необходимо прописать в системе и гите ssh-ключ.

Для обновления модуля: pip install --upgrade git+ssh://git@gitadress.com/qa/logger.git

Для установки (обновления) модуля из конкретной ветки: pip install (--upgrade) git+ssh://git@gitadress.com/qa/logger.git@branch_name

Для установки конкретного пакета используйте eggs: pip install git+ssh://git@gitadress.com/qa/logger.git@branch_name#egg=logger

```