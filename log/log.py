from logging import config
from logging import getLogger
from logcnofig import *


class Log:
    def __init__(self, logger_name):
        config.dictConfig(logging_dict)
        self.log = getLogger(logger_name)

    def debug(self, values):
        self.log.debug(values)

    def info(self, values):
        self.log.info(values)

    def error(self, values):
        self.log.error(values)

    def warning(self, values):
        self.log.warning(values)

    def critical(self, values):
        self.log.critical(values)


if __name__ == '__main__':
    my_log = Log('用户购买模块')
    my_log.warning('这是一条debugger信息')
