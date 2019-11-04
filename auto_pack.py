#! python3
# coding: UTF-8
# author: Camera360 QA team
# modify: 2019/11/4

'''
运行环境：
- python3.x
- requests库
- PIL库
- 以上两个库可用`pip3 install -r requirements.txt` 安装
- `pip install requests pillow`
脚本功能：
1.实现一键自动生成icon,上传并发布贴纸，清除商店缓存等操作
2.支持直接拖动一个文件夹,文件可以包含ios或者android贴纸
3.支持连续拖动单个贴纸
'''
import os
import zipfile
import time
import requests
import re
import math
from PIL import Image, ImageDraw, ImageFont
from threading import Timer

tuple_android = ('5d26d9fc217f27e935dbe739', 'android', (250, 215, 72))
tuple_ios = ('5daea0e7217f2727222d908b', 'ios', (179, 238, 58))

# 贴纸分类id，平台，背景颜色
(CATEGORY_ID, PLATFORM, BG_COLOR) = tuple_ios

# 是否是主题贴纸
IS_THEME = '1'  # '1' / '0'

CMS_COOKIES = dict(
    c360_oa_user_info="MmlNRGFrcWxMVXNkTzdDZzFzbjU1eVV4LzFBa2VTOUJoWjB2Y2xkZUx4MzIzMWtaamt0SUVTTGVhcXdXMU5oZkZFUHVpTlRPdDd5cURHMGhwUEdpZ3UyM20xNG9NSWNLZVBNZmhnbVFqcW54blF4Q3M0QkVOWHBkRHllUmhNeVIxL1JYYVdPenlTY09vdGxZQitlVm1TcjB0TWpqc1BWYTZ0R0hLQjd0V0xnMlFqSHRZN3VMbEE9PQ%3D%3D")
CMS_URL = r"https://comfort-qa.camera360.com"
UPLOAD_PIC_URL = r"/god/upload?utag=comm"
UPLOAD_ZIP_URL = r"/god/upload?utag=comm"
SUBMIT_URL = r"/god/transmit"

if os.path.exists(r"/System/Library/Fonts/PingFang.ttc"):
    FONT_TYPE = r"/System/Library/Fonts/PingFang.ttc"
elif os.path.exists(r"C:/Windows/Fonts/simhei.ttf"):
    FONT_TYPE = r"C:/Windows/Fonts/simhei.ttf"
elif os.path.exists(r"C:/Windows/Fonts/SIMYOU.TTF"):
    FONT_TYPE = r"C:/Windows/Fonts/SIMYOU.TTF"
else:
    print('没有找到字体路径')


def make_icon(path, name):
    # name去掉后缀  
    icon_name = re.split(r'-|_', name)[0]
    # 先假设取一个值，而得到比例
    font_size = 27
    font = ImageFont.truetype(FONT_TYPE, size=font_size)
    text_size_width = font.getsize(icon_name)[0]
    # 计算font_size:
    font_size_cal = math.floor(font_size * 190 / text_size_width)
    if font_size_cal > 50:
        font_size_cal = 50
    # font重新赋值
    font = ImageFont.truetype(FONT_TYPE, size=font_size_cal)
    text_size = font.getsize(icon_name)
    # 取画图的起始坐标点
    x = 100 - text_size[0] / 2
    y = 100 - text_size[-1] / 2
    # 画图
    img = Image.new("RGB", size=(200, 200), color=BG_COLOR)  # 创建图形
    draw = ImageDraw.Draw(img)
    draw.text((x, y), icon_name, font=font, fill='#191970')
    # 保存
    icon_path = os.path.join(path, name + '.png')
    img.save(icon_path)
    return icon_path


def upload_pic(pic_path):
    if os.path.isfile(pic_path):
        files = {'file': ("testfile.png", open(pic_path, 'rb'))}
        re = requests.post(CMS_URL + UPLOAD_PIC_URL, cookies=CMS_COOKIES, files=files,
                           data={"file_name": os.path.basename(pic_path)})
        # re.raise_for_status()
        re_json = re.json()
        if re_json['status'] == 200:
            return re_json['data']['fileName']
        else:
            print('图片上传失败！err: ' + re_json['message'])
            return False
    else:
        print('图片不存在！')
        return False


def upload_zip(zip_path):
    if os.path.isfile(zip_path):
        files = {'file': ("testfile-" + PLATFORM + ".zip", open(zip_path, 'rb'),
                          'application/x-zip-compressed')}
        re = requests.post(CMS_URL + UPLOAD_ZIP_URL, cookies=CMS_COOKIES, files=files,
                           data={"file_name": os.path.basename(zip_path)})
        # re.raise_for_status()
        re_json = re.json()
        if re_json['status'] == 200:
            return re_json['data']
        else:
            print('zip包上传失败! err: ' + re_json['message'])
            return False
    else:
        print('zip包不存在！')
        return False


def has_music(zip_path):
    if os.path.isfile(zip_path):
        zip_file = zipfile.ZipFile(zip_path, 'r')
        index_file = zip_file.namelist()[-1]
        content = zip_file.read(index_file)
        if b'"hasMusic": true' in content:
            return True
        else:
            return False
    else:
        print('音乐文件不存在！')
        return False


def submit_sticker_api(pic_url, zip_data, platform, sticker_name, category_id, has_music=False, is_theme='1'):
    music_tag = '1' if has_music else '0'
    pay_load = {
        'tags[0][parent_tag_name]': '头像',
        'tags[0][children_tag_names]': '大头',
        'appName': 'camera360',
        'product': 'camera360',
        'platform': platform,
        'name': sticker_name,
        'display_name': sticker_name,
        'onsale_time': str(int(time.time())),
        'off_time': '1665381400',
        'lang_arr': 'en,zh_cn,zh,th,ja,in,vi,ko,pt,pt_br,es,es_es,es_mx,ru,hi,ar,tr,de,de_de,other',
        'version_ctrl_info': '{"from":"810","not_support":[],"support":[],"to":"0","type":1}',
        'ctrl_down_info': '{"unlock_type":"1"}',
        'zip_url': zip_data['fileName'],
        'zip_md5': zip_data['fileMd5'],
        'zip_name': sticker_name + ".zip",
        'icon': pic_url,
        'topics_ids': category_id,
        'music_tag': music_tag,
        'is_theme': is_theme,
        'vip': '0',
        'icon_tag': '0',
        'ctrl_channe': '',
        'ctrl_area': '',
        'exclude_area': '',
        'ctrl_install_info': '',
        'transUrl': 'https://bmall-qa.camera360.com/backend/unity/saveProducts'
    }

    re = requests.post(CMS_URL + SUBMIT_URL, data=pay_load, cookies=CMS_COOKIES)
    # re.raise_for_status()
    re_json = re.json()
    if re_json['status'] == 200:
        print("pid:" + re_json['data']['pid'])
        return re_json['data']['pid']
    else:
        print("上传贴纸失败! err: " + re_json['message'])


# 上传单个贴纸
def submit_sticker(zip_path):
    # 获取并上传zip包
    zip_data = upload_zip(zip_path)
    if zip_data:
        # 获取并上传icon图
        sticker_name = os.path.basename(zip_path).split('.')[0]
        global CATEGORY_ID
        global PLATFORM
        global BG_COLOR
        if 'ios' in sticker_name.lower():
            (CATEGORY_ID, PLATFORM, BG_COLOR) = tuple_ios
        elif 'android' in sticker_name.lower():
            (CATEGORY_ID, PLATFORM, BG_COLOR) = tuple_android
        else:
            print('无法通过贴纸:', sticker_name, '的名字来判断是ios还是android平台！')
            return
        icon_path = make_icon(os.path.dirname(zip_path), sticker_name)
        print("save icon to :" + icon_path)
        pic_url = upload_pic(icon_path)
        # 提交贴纸
        if pic_url:
            stick_id = submit_sticker_api(pic_url, zip_data, PLATFORM, sticker_name, CATEGORY_ID,
                                          has_music=has_music(zip_path), is_theme=IS_THEME)
    return stick_id, sticker_name


# 连续上传文件或者文件夹
def continuous_upload():
    dict = {}
    loop = True
    while loop:
        path = input(r"请输入/拖入文件或者文件夹: ").strip()
        # 处理mac中文件夹名为空格的情况
        if r'\ ' in path:
            path = path.replace(r'\ ', ' ')
        # windwos中路径开头结尾出现双引号的情况
        if r'"' in path:
            path = path.replace(r'"', '')
        if os.path.exists(path) and os.path.isfile(path) and os.path.basename(path).endswith(
                '.zip') and not os.path.basename(path).startswith('.'):
            (key, value) = submit_sticker(path)
            dict[key] = value
        elif os.path.exists(path) and os.path.isdir(path):
            loop = False
            for i in os.listdir(path):
                if i.endswith('.zip') and not i.startswith('.'):
                    fullpath = os.path.join(path, i)
                    (key, value) = submit_sticker(fullpath)
                    dict[key] = value
        else:
            print("err msg: 'Path not exists or file is illegal.'")
        if loop:
            value = input("继续上传? (y/n) ").strip()
            if value != 'y' and value != 'Y':
                loop = False
    return dict


# 获取贴纸状态
def sticker_status(pid, name):
    pay_load = {
        'appName': 'camera360',
        'product': 'camera360',
        'guid': pid,
        'is_theme': "all",
        'locale': "",
        'name': "",
        'page': 1,
        'pageSize': 20,
        'platform': "all",
        'status': "all",
        'topics_id': "",
        'unlock_type': "all",
        'vip': "all",
        'transUrl': 'https://bmall-qa.camera360.com/backend/unity/products'
    }
    re = requests.post(CMS_URL + SUBMIT_URL, data=pay_load, cookies=CMS_COOKIES)
    # re.raise_for_status()
    re_json = re.json()
    if re_json['status'] == 200:
        if re_json['data']['lists'][0]['pid'] == pid:
            return re_json['data']['lists'][0]['status']
        else:
            print('没有找到贴纸:', name, '状态')
    else:
        print("贴纸状态获取失败：" + re_json['message'])


def sticker_publish_api(pid, name):
    pay_load = {
        'appName': 'camera360',
        'product': 'camera360',
        'pidArr[0]': pid,
        'type': "publish",
        'transUrl': 'https://bmall-qa.camera360.com/backend/unity/productsHandle'
    }
    re = requests.post(CMS_URL + SUBMIT_URL, data=pay_load, cookies=CMS_COOKIES)
    # re.raise_for_status()
    re_json = re.json()
    if re_json['status'] == 200:
        if sticker_status(pid, name) == 2:
            print('贴纸:', name, '发布成功')
    else:
        print("贴纸正式发布失败! err:" + re_json['message'])


# 状态： 0：打包状态 6：灰度 2：已上线 3：已下线 
# 定时间间隔去检查返回的字典：
def check_sticker_dict(dict):
    resdict = dict.fromkeys(dict.keys(), 0)
    for pid, name in dict.items():
        value = sticker_status(pid, name)
        if value == 2:
            resdict[pid] = 1
        elif value == 6:
            sticker_publish_api(pid, name)
        elif value == 0:
            print('贴纸:', name, '状态为：打包中，等待15s后检查...')
            print('....')
    resSet = set(resdict.values())
    if 0 in resSet:
        t = Timer(15, check_sticker_dict, (dict,))
        t.start()
    elif 1 in resSet and len(resSet) == 1:
        update_cache_api()
        print('所有', len(dict.keys()), '款贴纸已经上传并发布成功，可以开始测试了！')


# 更新商店缓存
def update_cache_api():
    pay_load = {
        'appName': 'camera360',
        'product': 'camera360',
        'transUrl': 'https://bmall-qa.camera360.com/backend/products/clear-cache'
    }
    re = requests.post(CMS_URL + SUBMIT_URL, data=pay_load, cookies=CMS_COOKIES)
    # re.raise_for_status()
    re_json = re.json()
    if re_json['status'] == 200:
        print('更新商店缓存成功！')
    else:
        print("更新商店缓存失败! err:" + re_json['message'])


if __name__ == "__main__":
    sticker_dict = continuous_upload()
    check_sticker_dict(sticker_dict)
