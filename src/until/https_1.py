# !/usr/bin/env python
# encoding: utf-8
"""
 @author: captain
 @file: logger.py
 @time: 2022/4/14
 @desc: 网络请求
 """

import requests
import json
import os
from requests_toolbelt import MultipartEncoder
from python.util.logger import Logger
from python.util.timer import Timer

log = Logger()


class Https:
    timeout = 10

    @staticmethod
    def __send_data(request_type, url, api, request, header: dict, **kwargs):
        """
        发送http请求
        :param request_type: get/post
        :param url: url或全域名
        :param api: 二级域名
        :param request:
        :param header:
        :param **kwargs, params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None
        :return: response:dict, e: code, result, start_time, response_time, json
        """
        content_type = None
        response = {}
        response_time = None
        r = None
        result_json = None
        code = 0  # -100为请求超时
        start_time = Timer.get_time(False)
        if url.endswith('/'):
            url = url[0:-1]
        elif api.startswith('/'):
            api = api[1:]
        if api == '':
            url_api = url
        else:
            url_api = url + '/' + api
        log.info('请求地址:{0}'.format(url_api))
        log.info('请求类型:%s' % request_type)
        log.info('请求内容:{0}'.format(request))
        if header is not None:
            log.info('请求头:{0}'.format(header))
            content_type = 'application/x-www-form-urlencoded'
            if 'Content-Type' in header:
                content_type = header['Content-Type']
            else:
                for key, value in header.items():
                    if key.lower() == 'content-type':
                        content_type = value
                        break
        try:
            if request_type == 'post':
                if type(request) == MultipartEncoder:
                    log.info('use MultipartEncoder to requests')
                    r = requests.post(url_api, data=request, headers=header, timeout=Https.timeout, **kwargs)
                else:
                    if content_type is not None:
                        # dict,上传文件request_files = {'file123': ('1.jpg', open('D:/tmp/1.jpg', 'rb'))}
                        if content_type.find(
                                'multipart/form-data') > -1:
                            if 'request_files' in request:
                                request_files = request.pop('request_files')
                            else:
                                request_files = None
                            r = requests.post(url_api, data=request, files=request_files, headers=header,
                                              timeout=Https.timeout, **kwargs)
                        # str,'<?xml  ?>' str
                        elif content_type.find('text/xml') > -1:
                            r = requests.post(url_api, data=request, headers=header, timeout=Https.timeout, **kwargs)
                        # dict,list
                        elif content_type.find('application/json') > -1:
                            r = requests.post(url_api, json=request, headers=header, timeout=Https.timeout, **kwargs)
                        # dict,files={'file':open('test.xls','rb')}
                        elif content_type.find('binary') > -1:
                            r = requests.post(url_api, files=request, headers=header, timeout=Https.timeout, **kwargs)
                        # dict,默认application/x-www-form-urlencoded
                        else:
                            r = requests.post(url_api, data=request, headers=header, timeout=Https.timeout, **kwargs)
                    else:
                        # dict,
                        r = requests.post(url_api, data=request, headers=header, timeout=Https.timeout, **kwargs)
            elif request_type == 'get':
                r = requests.get(url_api, params=request, headers=header, timeout=Https.timeout, **kwargs)
            # 响应处理
            log.info('响应timeout为:{0}s'.format(Https.timeout))
            response_time = int(r.elapsed.total_seconds() * 1000)
            code = r.status_code
            log.info('响应码:{0}, 响应时间{1}毫秒'.format(code, response_time))
            content_type = r.headers['Content-Type']
            log.info("响应数据类型为: " + content_type)
            log.info("响应数据头为: {0}".format(r.headers))
            if code == 200:
                if content_type.find('image') > -1:
                    log.info("响应数据为image，不做json()操作")
                elif content_type.find('application') > -1:
                    log.info("响应数据为application，不做json()操作")
                else:
                    try:
                        result_json = r.json()
                    except json.decoder.JSONDecodeError as e:
                        result_json = None
                    if result_json is not None:
                        result_text = json.dumps(result_json, indent='\t')
                        log.info('响应内容为json:\n{0}'.format(
                            result_text if result_text.__len__() < 1000 else result_text[0:1000]))
                    else:
                        json_text = str(r.text)
                        log.info(
                            '响应内容为非json:\n{0}'.format(json_text if json_text.__len__() < 1000 else json_text[0:1000]))
            r.raise_for_status()
        except requests.exceptions.Timeout as e:
            log.error('请求超时:{0}秒'.format(Https.timeout))
            code = -100
            result_json = {'code': code, 'https': '请求超时:{0}秒'.format(Https.timeout)}
        except requests.exceptions.RequestException as e:
            log.error('请求异常:{0}'.format(e))
            result_json = {'code': code, 'https': '请求异常:{0}'.format(e)}
        response['code'] = code
        response['result'] = r
        response['start_time'] = Timer.get_time_by_timestamp(start_time / 1000)  # 请求开始时间
        response['response_time'] = response_time if response_time is not None else (
                Timer.get_time(False) - start_time)
        response['json'] = result_json
        response['content_type'] = content_type
        return r

    @staticmethod
    def post(url: str = '', api: str = '', request=None, header: dict = None, **kwargs):
        return Https.__send_data('post', url, api, request, header, **kwargs)

    @staticmethod
    def get(url: str = '', api: str = '', request=None, header: dict = None, **kwargs):
        return Https.__send_data('get', url, api, request, header, **kwargs)

    @staticmethod
    def put(url, **kwargs):
        """
        封装put方法
        :param url:
        :param kwargs:
        :return:
        """
        data = kwargs.get("data")
        json_file = kwargs.get("json")
        files = kwargs.get("files")
        headers = kwargs.get("headers")
        cookies = kwargs.get("cookies")
        try:
            log.info("put请求的url:{}".format(url))
            log.info("put请求的data:{}".format(data))
            res = requests.put(url=url, data=data, json=json_file, headers=headers, cookies=cookies, files=files)
            if res.text == "Service Unavailable":
                log.error("post请求{}，有服务未响应".format(url))
                raise Exception("有服务未响应")
            else:
                return res
        except Exception as e:
            raise Exception(e)

    @staticmethod
    def download(url: str, save_path: str):
        file_path = save_path + '/' + url[url.rindex('/') + 1:][-20:]
        if os.path.isdir(save_path):
            pass
        elif os.path.isfile(save_path):
            file_path = save_path
        else:
            folder_path = os.path.dirname(save_path)
            log.info('folder_path:' + folder_path)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            if not os.path.basename(save_path) == '':
                file_path = save_path
        log.info('save file in: ' + file_path)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            os.remove(file_path)
        response = Https.get(url, '')
        save_file = open(file_path, 'wb')
        if response['code'] == 200:
            for chunk in response['result'].iter_content(100000):
                save_file.write(chunk)
        save_file.close()


if __name__ == '__main__':
    Https.get("https://www.baidu.com/")
