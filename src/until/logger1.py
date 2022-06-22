# !/usr/bin/env python
# encoding: utf-8
"""
 @author: captain
 @file: logger.py
 @time: 2022/4/14
 @desc: 日志记录
 """

import os
import logging
import logging.handlers


class Logger(logging.Logger):
    def __init__(self, name: str = "new", log_path=None, detail=False):
        super().__init__(name)
        # create formatter
        fmt = "%(asctime)s %(filename)s-Line:%(lineno)d [%(levelname)s]: %(message)s"
        if detail is True:
            fmt = "[%(asctime)s] - %(filename)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[" \
                  "process:%(process)s] - %(message)s "
        fmt_time = "%Y-%m-%d %H:%M:%S"
        formatter = logging.Formatter(fmt, fmt_time)

        # 控制台输出
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(formatter)
        self.addHandler(console_handler)

        # 写入文件
        if log_path is not None:
            if "log" in log_path:
                log_file_path = os.path.abspath(log_path)
            else:
                log_file_path = os.path.join(os.path.abspath(log_path), 'logs')
            if not os.path.exists(log_file_path):
                os.makedirs(log_file_path)
            log_file_name = os.path.join(log_file_path, 'log.txt')
            output_handler = logging.handlers.RotatingFileHandler(filename=log_file_name, encoding='utf-8',
                                                                  maxBytes=10 * 1024 * 1024, backupCount=10)
            output_handler.setLevel(logging.DEBUG)
            output_handler.setFormatter(formatter)
            self.addHandler(output_handler)


if __name__ == '__main__':
    log1 = Logger()
    log2 = Logger()
    log1.error("测试失败")
    log2.info('test')
    print(id(log1) == id(log2))
