# --------------------------------------
# Default logging configs and handlers
# --------------------------------------


def get_logconf(log_dir):
    return {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'default': {
                'format': '\t'.join([
                    'level:%(levelname)s',
                    'asctime:%(asctime)s',
                    'message:%(message)s',
                ]),
            },
        },
        'handlers': {
            'file': {
                'level': 'INFO',
                'class': 'logging.FileHandler',
                'filename': str(log_dir / 'kaz.log'),
                'formatter': 'default'
            },
        },
        'loggers': {
            'kaz': {
                'handlers': ['file'],
                'level': 'INFO',
            }
        }
    }
