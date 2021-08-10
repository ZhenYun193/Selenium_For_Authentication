# 日志配置文件
standard_format_for_file = '[日志时间：%(asctime)s][%(threadName)s:%(thread)d][日志名称:%(name)s][模块名称：%(filename)s]' \
                           '[执行行号：%(lineno)d][日志等级：%(levelname)s][提示信息：%(message)s}'
standard_format_for_console = """
{日志时间：%(asctime)s；
%(threadName)s:%(thread)d；
日志名称：%(name)s；
模块名称：%(filename)s；
执行行号：%(lineno)d；
日志等级：%(levelname)s；
提示信息：%(message)s}
"""
simple_format = '[日志时间：%(asctime)s][日志名称:%(name)s][日志等级：%(levelname)s][提示信息：%(message)s}'
test_format = '日志时间：%(asctime)s][提示信息：%(message)s}'
handler_log_level = 'DEBUG'
handler_file_path = './cache/debuggerlog.log'
handler_file_size = 1024*1024*5
handler_file_count = 5
loggers_handlers = ['console']
loggers_level = 'DEBUG'

logging_dict = {
    # 必选项，其值是一个整数值，表示配置格式的版本，当前唯一可用的值就是1
    'version': 1,
    # 可选项，其值是一个字典对象，该字典对象每个元素的key为要定义的过滤器名称，value为过滤器的配置信息组成的dict，如name
    'filters': {},
    # 可选项，默认值为True。该选项用于指定是否禁用已存在的日志器loggers，如果incremental的值为True则该选项将会被忽略
    'disable_existing_loggers': False,
    # 日志输出的格式
    # 可选项，其值是一个字典对象，该字典对象每个元素的key为要定义的格式器名称，value为格式器的配置信息组成的dict，如format和datefmt
    'formatters': {
        # 标准格式
        'standard_file': {'format': standard_format_for_file},
        'standard_console': {'format': standard_format_for_console},
        # 简单格式
        'simple': {'format': simple_format},
        # 测试格式
        'test': {'format': test_format},
    },
    # 日志的接收对象
    # 可选项，其值是一个字典对象，该字典对象每个元素的key为要定义的处理器名称，value为处理器的配置信息组成的dict，
    # 如class、level、formatter和filters，其中class为必选项，其它为可选项；其他配置信息将会传递给class所指定
    # 的处理器类的构造函数，如下面的handlers定义示例中的stream、filename、maxBytes和backupCount等
    'handlers': {
        # 打印到终端
        'console': {
            'level': handler_log_level,
            'class': 'logging.StreamHandler',
            'formatter': 'standard_console'
        },
        # 保存到文件
        'file': {
            'level': handler_log_level,
            'class': 'logging.FileHandler',
            'formatter': 'standard_file',
            'filename': handler_file_path,
            'encoding': 'utf-8'
        },
        # 保存文件，日志轮转：文件大小到达指定大小后，新建文件
        'default': {
            'level': handler_log_level,
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'standard_file',
            'filename': handler_file_path,
            # 设置文件大小
            'maxBytes': handler_file_size,
            # 保存文件个数
            'backupCount': handler_file_count,
            'encoding': 'utf-8'
        }
    },
    # loggers:日志的产生者，将日志传输给handler
    # 可选项，其值是一个字典对象，该字典对象每个元素的key为要定义的日志器名称，value为日志器的配置信息组成的dict，
    # 如level、handlers、filters 和 propagate
    'loggers': {
        # ’‘：日志的名字，有getLogger传参是决定
        '': {
            # handlers的接受者，可以填多个
            'handlers': [*loggers_handlers],
            # loggers(第一层日志级别限制)-->handlers(第二层日志级别限制)
            'level': loggers_level,
            # 默认True，向上（更高level的logger）传递，通常设置为False
            'propagate': False
        }
    }
}
