# !/usr/bin/env python
# encoding: utf-8
"""
 @author: captain
 @file: yaml_until.py
 @time: 2022/05/29
 @desc: 读取yaml文件
 """

import yaml
import os

file_path = os.path.split(os.path.realpath(__file__))[0]
root_path = os.path.join(os.path.split(file_path)[0], "testdata")


class YamlUtil:
    @staticmethod
    def read_yaml(yaml_file, part=None):
        with open(os.path.join(root_path, yaml_file), encoding="utf-8")as f:
            value = yaml.load(f, Loader=yaml.FullLoader)
            if part is not None:
                return value[part]
            return value


if __name__ == '__main__':
    print(YamlUtil.read_yaml("biology_identification.yml", "bind"))
