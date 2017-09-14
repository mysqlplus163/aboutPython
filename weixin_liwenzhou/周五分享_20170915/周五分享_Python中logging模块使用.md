# Python中logging配置分享

今天给大家分享的是我职业生涯至今一直再用的一份Python logging配置。

无论是Python开发的后端程序还是基于Django的Web项目都可以使用这个logging配置。

废话不多说直接上代码：
 ```python

import os
import logging.config

# 定义三种日志输出格式 开始

standard_format = '[%(asctime) -s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]' \
                  '[%(levelname)s][%(message)s]'

simple_format = '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'

id_simple_format = '[%(levelname)s][%(asctime)s] %(message)s'

# 定义日志输出格式 结束

logfile_dir = os.path.dirname(os.path.abspath(__file__))  # log文件的目录

logfile_name = 'all2.log'  # log文件名

# 如果不存在定义的日志目录就创建一个
if not os.path.isdir(logfile_dir):
    os.mkdir(logfile_dir)

# log文件的全路径
logfile_path = os.path.join(logfile_dir, logfile_name)

# log配置字典
LOGGING_DIC = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': standard_format,
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
        'simple': {
            'format': simple_format
        },
    },
    'filters': {},
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',  # 打印到屏幕
            'formatter': 'simple'
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件。自动切日志
            'filename': logfile_path,  # 日志文件
            'maxBytes': 1024*1024*5,  # 日志大小 5M
            'backupCount': 5,  # 日志文件备份个数
            'formatter': 'standard',  # 使用的日志文件格式
            'encoding': 'utf-8',  # 日志文件的编码，再也不用担心中文log乱码了
        },
    },
    'loggers': {
        '': {
            'handlers': ['default', 'console'],  # 这里把上面定义的两个handler都加上，即log数据既写入文件又打印到屏幕
            'level': 'DEBUG',
            'propagate': True,  # 向上（更高level的logger）传递
        },
    },
}

logging.config.dictConfig(LOGGING_DIC)  # 导入上面定义的配置
logger = logging.getLogger(__name__)  # 生成一个log实例
logger.info('It works!')  # 记录该日志配置文件的运行状态

 ```

## 在后端程序使用

只需要将上述代码保存在`init_logging.py`文件中，并且在你程序的入口处引用该文件即可。

在你其他的py文件中，只要在文件开头如下：
```python
import logging

logger = logging.getLogger("__name__")  # 生成一个以当前模块名为名字的logger实例
```

然后在需要写日志的地方：
```python
logger.debug("...")  # 记录debug日志
logger.info("...")  # 记录info日志
logger.warning("...")  # 记录warning日志
logger.error("...")  # 记录error日志
```

## 在Django项目中使用

只需要将上述logging配置，整理成一个字典，放到`your/project/settings.py中即可：

```python
# settings.py

# 在settings.py文件中添加如下LOGGING配置项

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '[%(asctime)s][%(threadName)s:%(thread)d][task_id:%(name)s][%(filename)s:%(lineno)d]'
                      '[%(levelname)s][%(message)s]'
        },
        'simple': {
            'format': '[%(levelname)s][%(asctime)s][%(filename)s:%(lineno)d]%(message)s'
        },
        'collect': {
            'format': '%(message)s'
        }
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_info.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 3,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_err.log"),  # 日志文件
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'standard',
            'encoding': 'utf-8',
        },
        'collect': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',  # 保存到文件，自动切
            'filename': os.path.join(BASE_LOG_DIR, "xxx_collect.log"),
            'maxBytes': 1024 * 1024 * 50,  # 日志大小 50M
            'backupCount': 5,
            'formatter': 'collect',
            'encoding': "utf-8"
        }
    },
    'loggers': {
       # 默认的logger应用如下配置
        '': {
            'handlers': ['default', 'console', 'error'],  # 上线之后可以把'console'移除
            'level': 'DEBUG',
            'propagate': True,
        },
        # 名为 'collect'的logger还单独处理
        'collect': {
            'handlers': ['console', 'collect'],  # 上线之后可以把'console'移除
            'level': 'INFO',
        }
    },
}

```

按如上配置好之后，就可以在Django项目的py文件中和之前一样生成logger实例，并使用了。

例如：
```python
# 在views.py中

import logging

logger = logging.getLogger("__name__")  # 生成一个以当前模块名为名字的logger实例
c_logger = logging.getLogger("collect")  # 生成一个名为'collect'的logger实例，用于收集一些需要特殊记录的日志
```

## 最后附上我翻译的Python官网的日志流图

