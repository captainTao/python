# !/usr/bin/env python
# encoding: utf-8
"""
 @author: captain
 @file: excel_until.py
 @time: 2022/07/01
 @desc: excel读取处理
"""
import os
import ast
import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.worksheet import Worksheet
from python.util.logger import Logger

log = Logger()


def excel_path(module):
    file_path = os.path.split(os.path.realpath(__file__))[0]
    root_path = os.path.split(file_path)[0]
    test_path = os.path.join(root_path, "testdata", "test_app_data")
    test_file = {
        'gen': ['test_data_g'],
        'aw': ['test_data_l'],
        'cl': ['test_data_li'],
        'st': ['test_dat', 'xxx.xlsx'],
        'cl': ['test_data_p'],
        'up': ['test_data_u']
    }
    return os.path.join(test_path, test_file[module][0], test_file[module][1])


class ExcelHandler:
    def __init__(self, module):
        self.filename = excel_path(module)
        log.info(f"read file path: {self.filename}")

    def open_sheet(self, sheet_name) -> Worksheet:
        """打开excel"""
        wb = load_workbook(self.filename)
        return wb[sheet_name]

    def read_headers(self, sheet_name="Sheet1"):
        """返回表头，为一个列表"""
        sheet = self.open_sheet(sheet_name)
        headers = []
        for header in sheet[1]:
            headers.append(header.value)
        log.info(f'excel headers: {headers}')
        return headers

    def read_rows(self, sheet_name="Sheet1"):
        """返回表的内容,为一个二维列表"""
        sheet = self.open_sheet(sheet_name)
        rows = list(sheet.rows)[1:]
        data = []
        for row in rows:
            row_data = []
            if row[0].value is None:
                break
            '''
            for cell in row:
                try:
                    row_data.append(eval(cell.value))
                except Exception as e:
                    log.debug(e)
                    row_data.append(cell.value)
            '''
            for index in range(len(row)):
                val = row[index].value
                if index > 1 and type(val) == str:
                    row_data.append(ast.literal_eval(val))
                else:
                    row_data.append(val)
            data.append(row_data)
        return data

    def read_excel_list(self, sheet_name="Sheet1"):
        """返回表所有内容，以字典形列表"""
        headers = self.read_headers(sheet_name)
        data = self.read_rows(sheet_name)
        return [dict(zip(headers, row_data)) for row_data in data]

    def read_excel_line(self, loc: str = None, **kwargs):
        """利用pandas来读取excel,返回也是字典列表"""
        excel_content = pd.read_excel(self.filename, index_col='case_id', engine='openpyxl', **kwargs)
        excel_content.insert(0, 'case_id', excel_content.index)
        headers = excel_content.columns.values
        log.info(f'excel shape: {excel_content.shape}')
        log.debug(f'excel headers: {headers.tolist()}')
        log.debug(f'excel index: {excel_content.index.tolist()}')
        if loc is not None:
            vls = excel_content.loc[loc]
            if isinstance(vls, pd.Series):
                vls = vls.values
                for index in range(len(vls)):
                    if index > 1 and type(vls[index]) == str:
                        vls[index] = ast.literal_eval(vls[index])
                    if pd.isna(vls[index]):
                        vls[index] = None
                return [dict(zip(headers, vls))]
        else:
            vls = excel_content
        vls_new = []
        for row_id, row in vls.iterrows():
            row = row.tolist()
            for index in range(len(row)):
                if index > 1 and type(row[index]) == str:
                    row[index] = ast.literal_eval(row[index])
                if pd.isna(row[index]):
                    row[index] = None
            vls_new.append(row)
        return [dict(zip(headers, row_data)) for row_data in vls_new]


if __name__ == '__main__':
    '''
    result1 = ExcelHandler('store').read_excel_list()
    print(result1)
    '''
    result2 = ExcelHandler('store').read_excel_line('life_store_04')
    print(result2)

