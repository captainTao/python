import os
import logging
import logging.handlers
import threading


class Logger(logging.Logger):
    _instance_lock = threading.Lock()

    def __init__(self, log_path=None, process=False):
        """
        初始化
        :param log_path: 日志保存路径
        :return:
        """
        super(Logger, self).__init__(self)
        if process:
            log_format = "[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[" \
                         "process:%(process)s] - %(message)s "
        else:
            log_format = "%(asctime)s %(filename)s-Line:%(lineno)d [%(levelname)s]: %(message)s"
        data_format = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(log_format, data_format)
        # 控制台输出log
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.addHandler(console_handler)
        # 写入文件log
        if log_path is not None:
            log_file_path = os.path.abspath(log_path) + '/logs'
            if not os.path.exists(log_file_path):
                os.makedirs(log_file_path)
            output_handler = logging.handlers.RotatingFileHandler(filename=log_file_path + '/log.txt', encoding='utf-8',
                                                                  maxBytes=10 * 1024 * 1024, backupCount=10)
            output_handler.setLevel(logging.DEBUG)
            output_handler.setFormatter(formatter)
            self.addHandler(output_handler)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with cls._instance_lock:
                if not hasattr(cls, '_instance'):
                    cls._instance = object.__new__(cls)
            return cls._instance
        return cls._instance


if __name__ == '__main__':
    log1 = Logger()
    log2 = Logger()
    log3 = Logger()
    print(id(log1) == id(log2) == id(log3))
    log1.info('testlog')
