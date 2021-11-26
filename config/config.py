import os
import sys
import multiprocessing


class Config:

    GROUP_NAME = 'ubank'
    PROJECT_NAME = 'spider_pdf'

    WORKER_NUM = multiprocessing.cpu_count()
    # WORKER_NUM = 1
    SERVER_PORT = 8000

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    LOG_DIR = os.path.join(BASE_DIR, 'logs')
    os.makedirs(LOG_DIR, exist_ok=True)

    TIMEZONE = 'Asia/Shanghai'
    USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'

    HOST_LOCAL = '192.168.3.110'
    HOST_REMOTE = '192.168.3.110'

    MONGO_DICT = {
        'host': HOST_LOCAL,
        'port': 27017,
        'db': GROUP_NAME,
        'username': 'root',
        'password': 'Zhouhf873@',
    }


