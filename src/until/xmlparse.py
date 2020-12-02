import os
import logging
from lxml import etree


class XMLParse:
    """
    pip3 install lxml
    doc:http://lxml.de/api/index.html
    """

    def __init__(self):
        self.tree = etree.parse(self.xmlpath)
        self.xmlpath = self.xmlpath
        self.text = lambda text: text if text is not None else ''

    def set_doc(self, xmlpath: str):
        """
        加载xml文件
        :param xmlpath: 文件路径
        :return:
        """
        if os.path.isfile(self.xmlpath) and self.xmlpath.endswith('.xml'):
            logging.info('read XML file:{0}'.format(self.xmlpath))
            return True
        else:
            logging.info('load XML file failed:{0}'.format(self.xmlpath))
            return False

    def write_doc(self):
        """
        写入xml文件
        :return:
        """
        try:
            self.tree.write(self.xmlpath, encoding="UTF-8", xml_declaration=True, pretty_print=True)
            return True
        except Exception as e:
            logging.info('write XML file failed:{0}'.format(e.value))
        return False

    def add_root_element(self, key, value, property: dict):
        """
        在根目录添加新元素
        :param key:
        :param value:
        :param property:
        :return:
        """
        if self.tree is None:
            return False
        self.__add_element(self.tree.getroot(), key, value, property)
        return self.write_doc()

    def add_element_by_str(self, xpath, index, key, value, property: dict):
        """
        向XPATH节点写入一对键值
        :param xpath:
        :param index: 在第几个元素中插入,-1则全部插入
        :param key:
        :param property:
        :param value:
        :return:
        """
        if self.tree is None:
            return False
        nodes = self.tree.xpath(xpath)
        if nodes is not None:
            if index != -1 and len(nodes) > index:
                self.__add_element(nodes[index], key, value, property)
            elif index == -1:
                for node in nodes:
                    self.__add_element(node, key, value, property)
        return self.write_doc()

    def add_element_by_map(self, xpath, index, map: dict):
        """
        在xpath添加新元素
        :param xpath:
        :param index:在第几个元素中插入,-1则全部插入
        :param dict:
        :return:
        """
        if self.tree is None:
            return False
        nodes = self.tree.xpath(xpath)
        if nodes is not None:
            if index != -1 and len(nodes) > index:
                for key, value in map.items():
                    self.__add_element(nodes[index], key, value, None)
            elif index == -1:
                for node in nodes:
                    for key, value in map.items():
                        self.__add_element(node, key, value, None)
        return self.write_doc()

    def __add_element(self, node, key, value, property: dict):
        """
        在node节点增加一个子节点
        :param node:
        :param key:
        :param value:
        :param property:
        :return:
        """
        element = etree.SubElement(node, key)
        element.text = value
        if property is not None:
            for property_key, property_value in property.items():
                element.set(property_key, property_value)

    def get_list_by_xpath(self, xpath, index):
        """
        根据Xpath得到List
        :param xpath:
        :param index:
        :return:
        """
        list = []
        if self.tree is None:
            return list
        nodes = self.tree.xpath(xpath)
        if nodes is not None:
            if index != -1 and len(nodes) > index:
                for subnode in nodes[index].getchildren():
                    if isinstance(subnode.tag, str):
                        list.append(self.text(subnode.text))
            elif index == -1:
                for node in nodes:
                    for subnode in node.getchildren():
                        if isinstance(subnode.tag, str):
                            list.append(self.text(subnode.text))
        return list

    def get_map_by_xpath(self, xpath, index):
        """
        根据Xpath得到MAP
        :param xpath:
        :param index:
        :return:
        """
        map = {}
        if self.tree is None:
            return map
        nodes = self.tree.xpath(xpath)
        if nodes is not None:
            if index != -1 and len(nodes) > index:
                for subnode in nodes[index].getchildren():
                    if isinstance(subnode.tag, str):
                        map[subnode.tag] = self.text(subnode.text)
            elif index == -1:
                for node in nodes:
                    for subnode in node.getchildren():
                        if isinstance(subnode.tag, str):
                            map[subnode.tag] = self.text(subnode.text)
        return map

    def get_list_map_by_xpath(self, xpath, index, itemname):
        """
        根据Xpath及子项名称得到listMap
        :param xpath:
        :param index:
        :param itemname:
        :return:
        """
        list = []
        if self.tree is None:
            return list
        nodes = self.tree.xpath(xpath)
        if nodes is not None:
            if index != -1 and len(nodes) > index:
                for subnode in nodes[index].getchildren():
                    if subnode.tag == itemname:
                        map = {}
                        for subsubnode in subnode.getchildren():
                            if isinstance(subsubnode.tag, str):
                                map[subsubnode.tag] = self.text(subsubnode.text)
                        list.append(map)
            elif index == -1:
                for node in nodes:
                    for subnode in node.getchildren():
                        if subnode.tag == itemname:
                            map = {}
                            for subsubnode in subnode.getchildren():
                                if isinstance(subsubnode.tag, str):
                                    map[subsubnode.tag] = self.text(subsubnode.text)
                            list.append(map)
        return list

    def get_list_list_by_xpath(self, xpath, index, itemname):
        """
        根据Xpath及子项名称得到listMap
        :param xpath:
        :param index:
        :param itemname:
        :return:
        """
        list = []
        if self.tree is None:
            return list
        nodes = self.tree.xpath(xpath)
        if nodes is not None:
            if index != -1 and len(nodes) > index:
                for subnode in nodes[index].getchildren():
                    if subnode.tag == itemname:
                        sublist = []
                        for subsubnode in subnode.getchildren():
                            if isinstance(subsubnode.tag, str):
                                sublist.append(self.text(subsubnode.text))
                        list.append(sublist)
            elif index == -1:
                for node in nodes:
                    for subnode in node.getchildren():
                        if subnode.tag == itemname:
                            sublist = []
                            for subsubnode in subnode.getchildren():
                                if isinstance(subsubnode.tag, str):
                                    sublist.append(self.text(subsubnode.text))
                            list.append(sublist)
        return list

    def get_str_by_xpath(self, xpath, index):
        """
        根据Xpath得到String
        :param xpath:
        :param index:
        :return:
        """
        str = ''
        if self.tree is None:
            return str
        nodes = self.tree.xpath(xpath)
        if nodes is not None:
            if 0 <= index < len(nodes):
                str = self.text(nodes[index].text)
        return str

    def change_map_by_xpath(self, xpath, index, value_map: dict):
        """
        根据map及父节点名称XPath,修改子节点内容
        :param xpath:
        :param index:
        :param value_map:
        :return:
        """
        map = {}
        for key, value in value_map.items():
            map[key] = value
        if self.tree is None:
            return map
        nodes = self.tree.xpath(xpath)
        if nodes is not None:
            if index != -1 and len(nodes) > index:
                for subnode in nodes[index].getchildren():
                    for key, value in value_map.items():
                        if subnode.tag == key:
                            subnode.text = value
            elif index == -1:
                for node in nodes:
                    for subnode in node.getchildren():
                        for key, value in value_map.items():
                            if subnode.tag == key:
                                subnode.text = value
            self.write_doc()
        return map

    def change_str_by_xpath(self, xpath, index, value):
        """
        根据XPath及下标修改节点内容
        :param xpath:
        :param index:
        :param value:
        :return: 如果写入失败,则返回""
        """
        if self.tree is None:
            return value
        nodes = self.tree.xpath(xpath)
        if nodes is not None:
            if 0 <= index <= len(nodes):
                nodes[index].text = value
                self.write_doc()
        return value
