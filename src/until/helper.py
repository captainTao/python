import subprocess
import re
import os
import logging
import hashlib
import requests
import json
import shutil
import zipfile


class Helper:
    """
    帮助类,提供各种常用方法
    """

    @staticmethod
    def json_format(obj, by_indent='\t'):
        """
        排列json字符串
        :param by_indent:
        :param obj: str,dict,list ,默认按照indent=\t,(-1,0,1)
        :return: 非json格式字符串将返回str(obj)
        """
        text = ''
        if obj is not None:
            if isinstance(obj, list) or isinstance(obj, dict):
                text = json.dumps(obj, indent=by_indent)
            elif isinstance(obj, str):
                try:
                    text = json.dumps(json.loads(obj), indent=by_indent)
                except json.decoder.JSONDecodeError:
                    text = obj
        return text

    @staticmethod
    def ping(url, timeout=3):
        try:
            r = requests.get(url, timeout=timeout)
            return True
        except requests.exceptions.ReadTimeout as e:
            logging.error('无法连接url=%s,timeout=%s' % (url, timeout))
        return False

    @staticmethod
    def md5(data: str):
        """
        生成MD5
        :param data:
        :return:
        """
        return hashlib.md5(data.encode(encoding='utf-8')).hexdigest()

    @staticmethod
    def dict2list(data: dict):
        """
        将字典转化为列表
        :param data:
        :return: [(key,value),(key,value)]
        """
        keys = data.keys()
        vals = data.values()
        list = [(key, val) for key, val in zip(keys, vals)]
        return list

    @staticmethod
    def list2dict(data: list):
        """
        将列表转化为字典
        :param data:
        :return:
        """
        dict = {}
        for tup in data:
            dict[tup[0]] = tup[1]
        return dict

    @staticmethod
    def execute(cmd, cwd=None, env=None):
        """
        执行cmd命令,返回结果.
        :param env:
        :param cmd:
        :param cwd:
        :return:
        """
        global output, stdout, stderr
        try:
            output = subprocess.Popen(cmd, shell=True, cwd=cwd, env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = output.communicate()
        except Exception as e:
            logging.info('执行{0}出现异常'.format(cmd))
        finally:
            if output is not None:
                output.stdout.close()
                output.stderr.close()
                output.kill()
        out = None
        err = None
        if stdout is not None:
            out = str(stdout, encoding='utf-8')
        if stderr is not None:
            err = str(stderr, encoding='utf-8')

        logging.info('[info]: execute cmd: ' + cmd)
        logging.info('[info]: execute out: ' + out)
        logging.info('[info]: execute err: ' + err)
        return out, err

    @staticmethod
    def file_modify_by_regex(file, old_regex, new_str, new_name=None):
        """
        修改文件内容
        :param file: 文件地址
        :param old_regex: 正则表达式,需要修改的内容
        :param new_str: 新内容
        :param new_name: 新文件地址,None则表示在源文件上修改
        :return:
        """
        if os.path.isfile(file):
            with open(file, "r", encoding="utf-8") as f1, \
                    open("%s.temp" % file, "w", encoding="utf-8") as f2:
                for line in f1:
                    f2.write(re.sub(old_regex, new_str, line))
            if new_name is not None:
                os.rename("%s.temp" % file, os.path.dirname(file) + '/' + new_name)
            else:
                os.remove(file)
                os.rename("%s.temp" % file, file)
            return True
        else:
            logging.info('{0}读取异常'.format(file))
            return False

    @staticmethod
    def file_modify(file, old_str, new_str, new_name=None):
        """
        修改文件内容
        :param file: 文件地址
        :param old_str: 需要修改的内容
        :param new_str: 新内容
        :param new_name: 新文件地址,None则表示源文件上修改
        :return:
        """
        if os.path.isfile(file):
            with open(file, "r", encoding="utf-8") as f1, \
                    open("%s.temp" % file, "w", encoding="utf-8") as f2:
                for line in f1:
                    if old_str in line:
                        line = line.replace(old_str, new_str)
                    f2.write(line)
            if new_name is not None:
                os.rename("%s.temp" % file, os.path.dirname(file) + '/' + new_name)
            else:
                os.remove(file)
                os.rename("%s.temp" % file, file)
            return True
        else:
            logging.info('{0}读取异常'.format(file))
            return False

    @staticmethod
    def file_read_all(file):
        """
        读取文件内容
        :param file:
        :return:
        """
        text = ''
        if os.path.isfile(file):
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    text += line
        else:
            logging.info('{0}读取异常'.format(file))
        return text

    @staticmethod
    def copy_folder(src, des):
        # src 原始目录， des 目标目录
        src = os.path.normpath(src)
        des = os.path.normpath(des)
        if not os.path.exists(src):
            logging.error("复制文件路径不存在:" + src)
            return
        # 若是文件
        if os.path.isfile(src):
            if not os.path.exists(des):
                os.makedirs(des)
            shutil.copy(src, des)  # 第一个参数是文件，第二个参数目录
            return
        # 若是文件夹
        elif os.path.isdir(src):
            if os.path.exists(des):
                shutil.rmtree(des)  # 文件存在则删除文件夹
            shutil.copytree(src, des)  # 第一个参数是目录，第二个参数也是目录
        else:
            logging.error("复制文件出错")

    @staticmethod
    def __get_zip_file(input_path, result):
        """
        对目录进行深度优先遍历
        :param input_path:
        :param result:
        :return:
        """
        files = os.listdir(input_path)
        for file in files:
            if os.path.isdir(input_path + '/' + file):
                Helper.__get_zip_file(input_path + '/' + file, result)
            else:
                result.append(input_path + '/' + file)

    @staticmethod
    def zip_file_path(input_path, output_path, output_name):
        """
        压缩文件
        :param input_path: 压缩的文件夹路径
        :param output_path: 解压（输出）的路径
        :param output_name: 压缩包名称
        :return:
        """
        f = zipfile.ZipFile(output_path + '/' + output_name, 'w', zipfile.ZIP_DEFLATED)
        filelists = []
        Helper.__get_zip_file(input_path, filelists)
        for file in filelists:
            f.write(file)
        # 调用了close方法才会保证完成压缩
        f.close()
        return output_path + r"/" + output_name
