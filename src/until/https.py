import requests
import json
import os
from requests_toolbelt import MultipartEncoder
from src.util.logger import Logger
from src.util.timer import Timer

log = Logger()


class Https:
    """
      pip3 install requests
      基于requests
      """
    request_timeout = 60

    @staticmethod
    def __send_data(request_type, url, api, data, header: dict, **kwargs):
        """
        发送http请求
        :param request_type: get/post
        :param url: url或全域名
        :param api: 二级域名
        :param data:
        :param header:
        :param **kwargs, params=None, data=None, headers=None, cookies=None, files=None,
            auth=None, timeout=None, allow_redirects=True, proxies=None,
            hooks=None, stream=None, verify=None, cert=None, json=None
        :return: response:dict, e: code, result, start_time, response_time, json
        """
        if url.endswith('/'):
            url = url[0:-1]
        elif api.startswith('/'):
            api = api[1:]
        if api == '':
            url_api = url
        else:
            url_api = url + '/' + api
        content_type = None
        response = {}
        response_time = None
        r = None
        result_json = None
        code = 0  # -100为请求超时
        start_time = Timer.get_time(False)
        log.info('请求地址:{0}'.format(url_api))
        log.info('请求类型:%s' % request_type)
        log.info('请求内容:{0}'.format(data))
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
                if type(data) == MultipartEncoder:
                    log.info('use MultipartEncoder to requests')
                    r = requests.post(url_api, data=data, headers=header, timeout=Https.request_timeout, **kwargs)
                else:
                    if content_type is not None:
                        # dict,上传文件request_files = {'file123': ('1.jpg', open('D:/tmp/1.jpg', 'rb'))}
                        if content_type.find(
                                'multipart/form-data') > -1:
                            if 'request_files' in data:
                                request_files = data.pop('request_files')
                            else:
                                request_files = None
                            r = requests.post(url_api, data=data, files=request_files, headers=header,
                                              timeout=Https.request_timeout, **kwargs)
                        # str,'<?xml?>' str
                        elif content_type.find('text/xml') > -1:
                            r = requests.post(url_api, data=data, headers=header, timeout=Https.request_timeout,
                                              **kwargs)
                        # dict,list
                        elif content_type.find('application/json') > -1:
                            r = requests.post(url_api, json=data, headers=header, timeout=Https.request_timeout,
                                              **kwargs)
                        # dict,files={'file':open('test.xls','rb')}
                        elif content_type.find('binary') > -1:
                            r = requests.post(url_api, files=data, headers=header, timeout=Https.request_timeout,
                                              **kwargs)
                        # dict,默认application/x-www-form-urlencoded
                        else:
                            r = requests.post(url_api, data=data, headers=header, timeout=Https.request_timeout,
                                              **kwargs)
                    else:
                        # dict,
                        r = requests.post(url_api, data=data, headers=header, timeout=Https.request_timeout, **kwargs)
            elif request_type == 'get':
                r = requests.get(url_api, params=data, headers=header, timeout=Https.request_timeout, **kwargs)
            # 响应处理
            response_time = int(r.elapsed.total_seconds() * 1000)
            code = r.status_code
            log.info('响应码:{0}, 响应时间{1}毫秒'.format(code, response_time))
            content_type = r.headers['Content-Type']
            log.info("请求数据类型为: " + content_type)
            if code == 200:
                if content_type.find('image') > -1:
                    log.info("请求数据为image，不做json()操作")
                elif content_type.find('application') > -1:
                    log.info("请求数据为application，不做json()操作")
                else:
                    try:
                        result_json = r.json()
                    except json.decoder.JSONDecodeError as e:
                        result_json = None
                        log.info('json转化异常:{0}'.format(e))
                    if result_json is not None:
                        result_text = json.dumps(result_json, indent='\t', ensure_ascii=False)
                        log.info('响应内容为json:\n{0}'.format(
                            result_text if result_text.__len__() < 1000 else result_text[0:1000]))
                    else:
                        json_text = str(r.text)
                        log.info(
                            '响应内容非json:\n{0}'.format(json_text if json_text.__len__() < 1000 else json_text[0:1000]))
            r.raise_for_status()
        except requests.exceptions.Timeout as e:
            log.error('请求超时:{0}秒'.format(Https.request_timeout))
            code = -100
            result_json = {'code': code, 'https': '请求超时:{0}秒'.format(Https.request_timeout)}
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
    def post(url: str = '', api: str = '', data=None, header: dict = None, **kwargs):
        return Https.__send_data('post', url, api, data, header, **kwargs)

    @staticmethod
    def get(url: str = '', api: str = '', data=None, header: dict = None, **kwargs):
        return Https.__send_data('get', url, api, data, header, **kwargs)

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
    pass
