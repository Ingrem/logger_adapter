from sys import stdout
from copy import deepcopy
import logging
from logstash import UDPLogstashHandler, TCPLogstashHandler


class Logger(object):
    def __init__(self, service_name, log_level='info'):
        self.service_name = service_name

        self.logger = logging.getLogger(service_name)
        self.set_log_level(log_level)
        self.add_new_log_levels()
        self.format = '%(levelname)s %(asctime)s: %(message)s'

        sh = logging.StreamHandler(stream=stdout)
        sh.setFormatter(logging.Formatter(self.format))
        self.logger.addHandler(sh)

        self.extra = {
            'service': service_name
        }

    def add_new_log_levels(self):
        success_lvl = 11
        logging.addLevelName(success_lvl, "SUCCESS")

        def success(logger, message, *args, **kws):
            if logger.isEnabledFor(success_lvl):
                # Yes, log takes its '*args' as 'args'.
                logger._log(success_lvl, message, args, **kws)

        self.logger.success = success

        system_lvl = 12
        logging.addLevelName(system_lvl, "SYSTEM")

        def system(logger, message, *args, **kws):
            if logger.isEnabledFor(system_lvl):
                # Yes, log takes its '*args' as 'args'.
                logger._log(system_lvl, message, args, **kws)

        self.logger.system = system

    def set_log_level(self, log_level):
        if log_level == 'info':
            self.logger.setLevel(logging.INFO)
        elif log_level == 'debug':
            self.logger.setLevel(logging.DEBUG)
        elif log_level == 'critical':
            self.logger.setLevel(logging.CRITICAL)
        elif log_level == 'error':
            self.logger.setLevel(logging.ERROR)
        elif log_level == 'fatal':
            self.logger.setLevel(logging.FATAL)
        elif log_level == 'warn':
            self.logger.setLevel(logging.WARN)
        elif log_level == 'warning':
            self.logger.setLevel(logging.WARNING)

    def log_to_logstash(self, host, port, logstash_network='udp'):
        if logstash_network == 'udp':
            self.logger.addHandler(UDPLogstashHandler(
                host=host,
                port=port,
                version=1
            ))
        elif logstash_network == 'tcp':
            print('added tcp handler')
            self.logger.addHandler(TCPLogstashHandler(
                host=host,
                port=port,
                version=1
            ))

    def log_to_file(self, filename=None):
        if filename is None:
            filename = '{}.log'.format(self.service_name)
        fh = logging.FileHandler(filename)
        fh.setFormatter(logging.Formatter(self.format))
        self.logger.addHandler(fh)

    def update_extras(self, additional: dict):
        extra = deepcopy(self.extra)
        extra.update(additional)

    def log_to_redis(self, host, port, topic):
        """
        import redis only using here
        this handler send all logging msgs to redis pubsub

        :param host: redis host str
        :param port: redis port str
        :param topic: redis pubsub topic for logging
        :return: None
        """
        import redis

        class RedisHandler(logging.StreamHandler):
            def __init__(self):
                logging.StreamHandler.__init__(self)
                self.redis_db = redis.StrictRedis(host=host, port=port)

            def emit(self, record):
                msg = self.format(record)
                self.redis_db.publish(topic, msg)

        rh = RedisHandler()
        rh.setFormatter(logging.Formatter(self.format))
        self.logger.addHandler(rh)
        return rh

    def update_extras(self, additional: dict):
        extra = deepcopy(self.extra)
        extra.update(additional)
        return extra

    def success(self, msg, **extras):
        self.logger.success(self.logger, msg, extra=self.update_extras(extras))

    def system(self, msg, **extras):
        self.logger.system(self.logger, msg, extra=self.update_extras(extras))

    def info(self, msg, **extras):
        self.logger.info(msg, extra=self.update_extras(extras))

    def debug(self, msg, **extras):
        self.logger.debug(msg, extra=self.update_extras(extras))

    def critical(self, msg, **extras):
        self.logger.critical(msg, extra=self.update_extras(extras))

    def error(self, msg, **extras):
        self.logger.error(msg, extra=self.update_extras(extras))

    def fatal(self, msg, **extras):
        self.logger.fatal(msg, extra=self.update_extras(extras))

    def warning(self, msg, **extras):
        self.logger.warning(msg, extra=self.update_extras(extras))

    def metric(self, msg, **metrics):
        self.logger.info(msg, extra=self.update_extras(metrics))
