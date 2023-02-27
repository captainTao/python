# !/usr/bin/env python
# encoding: utf-8
"""
------------------------------------
# @FileName    :request_and_assert.py
# @Time        :2022/05/09
# @Author      :captain h wang
# @description :请求和断言
------------------------------------
"""
import allure
import requests
import re
from python.util.logger import Logger
from python.util.yaml_util import YamlUtil
from python.common.app_login import appLogin  # 用共用账号
from python.common.app_login_cap import AppLogin  # 用自己账号
from python.common.file_path import filePath
from python.common.get_token import get_str
from python.config.conf import server_ip
from requests.packages.urllib3.exceptions import InsecureRequestWarning

log = Logger()
env = "sit"
# appLogin().update_token()  # 用共用账号
AppLogin().update_token()  # 用自己账号
token = get_str(filePath().app_token_path())
Authorization = "Bearer " + token
log.info(f"Authorization = {Authorization}")


def request_data_and_assert(args, header_type=None, affirm=True, headers=None, params=None, json=None, data=None,
                            **kwargs):
    case_id = args.get('case_id', None)
    title = args['name']
    allure.dynamic.title(title)
    log.info(f"case_id = {case_id}, title = {title}")
    url = server_ip() + args["request"]["url"]
    method = args["request"]["method"]
    if headers is None:
        headers = get_headers(header_type)
    if params is None and "params" in args["request"]:
        params = args["request"]["params"]
        if type(params) == dict:
            items_list = []
            for key, value in params.items():
                items_list.append(f"{key}={value}")
            url = url + "?" + "&".join(items_list)
    if json is None and "body" in args["request"]:
        json = args["request"]["body"]
    if data is None and "data" in args["request"]:
        data = args["request"]["data"]
    validate = args["validate"] if "validate" in args else None
    extract = args["extract"] if "extract" in args else None
    log.info(f"request: headers = {headers}")
    log.info(f"request：url = {url}, method = {method}, params = {params}, json = {json}, data = {data}")
    log.info(f"request: kwargs = {kwargs}")
    log.info(f"validate = {validate}, extract = {extract}")
    try:
        log.info("发送请求.....")
        requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
        res = requests.request(url=url, method=method, headers=headers, json=json, data=data, verify=False,
                               **kwargs)
        code = res.status_code
        content_type = res.headers['Content-Type']
        log.info(f"response code：{code}, content_type: {content_type} ")
    except requests.exceptions.Timeout as e:
        log.error(f"请求超时： {e}, 用例没有被执行")
        assert False
    except Exception as e:
        log.error(f"请求异常：{e}, 用例没有被执行")
        assert False
    else:
        try:
            if content_type.find("application/json") > -1:
                log.info(f"response: {res.text}")
            if validate is not None and "status_code" in validate.keys():
                assert code == validate["status_code"]
                log.info(f"响应状态: {code}, 与校验值一致")
            if code == 200:
                log.info(f"响应状态:200, 请求正常...")
                if content_type.find("image") > -1:
                    log.info("响应为图片，不做json()处理")
                elif content_type.find("application/json") > -1 and validate is not None:
                    if not affirm:
                        log.debug(f"不做断言，只请求结果，直接返回response")
                        return res.json()
                    if "msg" in validate.keys():
                        assert res.json()["msg"] == validate["msg"]
                        msg = validate["msg"]
                        log.info(f"响应msg: {msg}, 与校验值一致")
                    if "code" in validate.keys():
                        assert res.json()["code"] == validate["code"]
                        res_code = validate["code"]
                        log.info(f"响应code码: {res_code}, 与校验值一致")
                    if "contains" in validate.keys():
                        contains = validate["contains"]
                        if type(contains) == list:
                            for contains_item in contains:
                                assert contains_item in res.text
                                log.info(f"响应包含: {contains_item}字段")
                        else:
                            assert contains in res.text
                            log.info(f"响应包含: {contains}字段")
                    if "equals" in validate.keys():
                        log.info('Mark: 只能校验返回json的data字典中第一层级key的值')
                        res_json = res.json()["data"]
                        for key in validate["equals"].keys():
                            assert res_json[key] == validate["equals"][key]
                            log.info(f"校验字段: '{key} = {res_json[key]}' 成功")
                    if extract is not None and type(extract) == dict:
                        log.info(f"extract_string = {extract}")
                        if 'all' in extract.keys():
                            log.info("提取所有返回的json()")
                            log.info(f"用例: {title}, 测试通过")
                            return res.json()
                        if 'data' in extract.keys():
                            log.info("提取所有返回的json data数据")
                            log.info(f"用例: {title}, 测试通过")
                            return res.json()['data']
                        extract_dict = {}
                        res_data = res.text
                        for key, match_str in extract.items():
                            if match_str == "" or match_str is None:
                                match_str = r'"{0}":(".*?"|\d*|.*)'.format(key)
                            if type(match_str) == str:
                                log.info(f"match_str = {match_str}")
                                # noinspection PyBroadException
                                try:
                                    regex = re.compile(r'{}'.format(match_str))
                                    match_result = regex.search(res_data).group(1)
                                except Exception as e:
                                    log.error(f"extract: 当前key: {key}没有匹配到结果")
                                    extract_dict[key] = None
                                else:
                                    log.info(f"extract: 当前key: {key}匹配到值为{match_result}")
                                    extract_dict[key] = match_result
                        log.info(f"提取数据：extract_result = {extract_dict}")
                        log.info(f"用例: {title}, 测试通过")
                        if len(extract_dict) > 1:
                            return extract_dict
                        elif len(extract_dict) == 1:
                            return list(extract_dict.values())[0]
            log.info(f"用例: {title}, 测试通过")
        except Exception as e:
            log.error(f"断言异常, {e}, 用例测试不通过")
            assert False
    finally:
        log.info(f"-" * 60)


def get_headers(header_type: str):
    headers = YamlUtil.read_yaml("base_config.yml", "headers", "config")
    headers["Authorization"] = Authorization
    headers["Package-Name"] = YamlUtil.read_yaml("base_config.yml", "Package-Name", "config")[env]
    content_type = {
        'json': 'application/json; charset=utf-8',
        'form_url': 'application/x-www-form-urlencoded',
        'form_data': 'multipart/form-data',
        'css': 'text/css',
        'js': 'application/javascript',
        'html': 'text/html; charset=utf-8',
        'text': 'text/plain; charset=UTF-8'
    }
    if header_type in content_type.keys():
        headers["Content-Type"] = content_type[header_type]
    if header_type not in content_type.keys() and header_type is not None:
        headers["Content-Type"] = header_type
    return headers
