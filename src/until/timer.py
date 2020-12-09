import datetime
import time


class Timer:

    @staticmethod
    def get_time(second=True):
        """
        返回当前时间戳,second=True返回秒时间戳10位,second=False返回毫秒时间戳13位
        :return:
        """
        if second is not True:
            return int(datetime.datetime.now().timestamp() * 1000)
        else:
            return int(datetime.datetime.now().timestamp())

    @staticmethod
    def get_time_for_file():
        """
        生成用于文件名称时间 %Y_%m%d_%H%M_%S
        :return:
        """
        return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

    @staticmethod
    def get_time_for_log():
        """
        生成用于日记的时间
        :return:
        """
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[0:-3]

    @staticmethod
    def get_time_for_date():
        """
        生成日期
        :return:
        """
        return datetime.datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def get_time_for_mouth_date():
        """
        生成日期
        :return:
        """
        return datetime.datetime.now().strftime('%m月%d日')

    @staticmethod
    def get_time_for_date_and_time():
        """
        生成日期
        :return:
        """
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_time_for_date_by_cus(strftime):
        """
        生成日期 ps:'%Y-%m-%d %H:%M:%S'
        :return:
        """
        return datetime.datetime.now().strftime(strftime)

    @staticmethod
    def get_time_by_timestamp_and_cus(strftime, time: int):
        """
        返回,ps:%Y-%m-%d %H:%M:%S
        :param strftime:
        :param time:时间戳
        :return:
        """
        return datetime.datetime.fromtimestamp(time).strftime(strftime)

    @staticmethod
    def get_time_by_timestamp(time: int):
        """
        返回%Y-%m-%d %H:%M:%S
        :param time:
        :return:
        """
        return datetime.datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def get_time_by_date_and_cus(strftime, time: str):
        """
        返回时间戳
        :param time: str
        :param strftime:
        :return:
        """
        return datetime.datetime.strptime(time, strftime).timestamp()

    @staticmethod
    def get_time_interval(startime: int, endtime: int):
        """
        计算时间差,返回X天X小时X分X秒
        :param startime:
        :param endtime:
        :return:
        """
        use_time = ''
        diff = endtime - startime
        if diff < 0:
            return '时间不正确'
        days = int(diff / (60 * 60 * 24))
        hours = int((diff - days * 60 * 60 * 24) / (60 * 60))
        mins = int((diff - days * 60 * 60 * 24 - hours * 60 * 60) / 60)
        seconds = int(diff - days * 60 * 60 * 24 - hours * 60 * 60 - mins * 60)
        if days > 0:
            use_time = use_time + str(days) + 'd'
        if hours > 0:
            use_time = use_time + str(hours) + 'h'
        if mins > 0:
            use_time = use_time + str(mins) + 'm'
        if seconds > 0:
            use_time = use_time + str(seconds) + 's'
        return use_time

    @staticmethod
    def get_days_interval(date1, date2):
        """
        返回两个时间的相差天数
        :param date1:
        :param date2:
        :return:
        """
        # %Y-%m-%d为日期格式，其中的-可以用其他代替或者不写，但是要统一，同理后面的时分秒也一样；可以只计算日期，不计算时间。
        # date1=time.strptime(date1,"%Y-%m-%d %H:%M:%S")
        # date2=time.strptime(date2,"%Y-%m-%d %H:%M:%S")
        if is_date(date1) and is_date(date2):
            date1 = time.strptime(date1, "%Y-%m-%d")
            date2 = time.strptime(date2, "%Y-%m-%d")
            # 根据上面需要计算日期还是日期时间，来确定需要几个数组段。下标0表示年，小标1表示月，依次类推...
            # date1=datetime.datetime(date1[0],date1[1],date1[2],date1[3],date1[4],date1[5])
            # date2=datetime.datetime(date2[0],date2[1],date2[2],date2[3],date2[4],date2[5])
            date1 = datetime.datetime(date1[0], date1[1], date1[2])
            date2 = datetime.datetime(date2[0], date2[1], date2[2])
            # 返回两个变量相差的值，就是相差天数
            return (date2 - date1).days

    @staticmethod
    def get_hour_now():
        """
        返回小时，24h制
        """
        return int(time.strftime('%H', time.localtime(time.time())))


def is_date(string):
    """
    验证日期是否有效
    :param string:
    :return:
    """
    try:
        time.strptime(string, "%Y-%m-%d")
        return True
    except:
        return False
