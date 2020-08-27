import logging
import logging.config
import logging.handlers
import glob
dict_config = {
        'version': 1,
        'formatters': {
            'detailed': {
                'class': 'logging.Formatter',
                'format': '%(asctime)s (%(levelname)s) : [%(name)s],%(filename)s:%(lineno)d %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': 'DEBUG',
            },
            'file': {
                'class': 'logging.FileHandler',
                'filename': 'info.log',
                'mode': 'w',
                'level': 'DEBUG',
                'formatter': 'detailed',
            },
        },
        'root': {
            'level': 'DEBUG',
            'handlers': ['console', 'file']
        },
    }

logging.config.dictConfig(dict_config)
LOG_FILENAME = 'info.log'
handler = logging.handlers.RotatingFileHandler(
              LOG_FILENAME, maxBytes=1024, backupCount=5)
