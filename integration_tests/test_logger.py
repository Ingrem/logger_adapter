from datetime import datetime
from log.app import Logger


logger = Logger(service_name="log-unit-test", log_level="debug")
logger.log_to_logstash(host="0.0.0.0", port=6004, logstash_network='udp')

logger.debug("debug log works; date: {}".format(datetime.now()))
logger.success("success log works; date: {}".format(datetime.now()))
logger.system("system log works; date: {}".format(datetime.now()))
logger.info("info log works; date: {}".format(datetime.now()))
logger.warning("warning log works; date: {}".format(datetime.now()))
logger.error("error log works; date: {}".format(datetime.now()))
logger.critical("critical log works; date: {}".format(datetime.now()))
logger.fatal("fatal log works; date: {}".format(datetime.now()))
