import time
import threading


class TimerTask(threading.Thread):

    def __init__(self, func, delay: int, period: int):
        """
        定时器
        :param func: 执行方法
        :param delay: 延迟启动,毫秒
        :param period: 每隔多少毫秒运行一次
        """
        threading.Thread.__init__(self)
        self.__delay_time = delay
        self.__period_time = period
        self.__stop = False
        self.__func = func

    def run(self):
        """
        开始运行任务
        :return:
        """
        self.__sleep(self.__delay_time)  # 延迟启动任务
        # 运行任务
        if self.__stop is False:
            self.__func()
        while self.__stop is False:  # 循环启动任务
            self.__sleep(self.__period_time)
            # 运行任务
            if self.__stop is False:
                self.__func()

    def __sleep(self, sleep_time):
        """
        切割等待时间,方便退出
        :param sleep_time:
        :return:
        """
        time_int = (int)(sleep_time / 1000)
        time_decimal = sleep_time / 1000 - time_int
        while time_int > 0 and self.__stop is False:
            time_int -= 1
            time.sleep(1)
        time.sleep(time_decimal)

    def cancel(self):
        """
        取消定时器
        :return:
        """
        self.__stop = True
