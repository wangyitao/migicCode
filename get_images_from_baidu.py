# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午9:44
# @Author  : Felix Wang

import re
import requests
import json
import random
from multiprocessing import Pool


def translate(content, tolang='zh', fromlang=None):
    User_Agent = [
        'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36',
        'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
        'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    ]
    url = 'https://fanyi.baidu.com/basetrans'

    headers = {
        'User-Agent': random.choice(User_Agent)
    }
    datas = {
        'query': content,
    }
    # 自动获取语言类型
    if not fromlang:
        fromlang = json.loads(requests.post('https://fanyi.baidu.com/langdetect', data=datas, headers=headers).text)[
            'lan']
    # print(fromlang)
    data = {
        'from': fromlang,
        'to': tolang,
        'query': content,

    }

    try:
        res = requests.post(url=url, data=data, headers=headers)
        # print(res.text)
        result = json.loads(res.text)
        return result['trans'][0]['dst']
    except Exception as e:
        print('翻译出错')
        print(e)


'''
zh    中文
en    英语
yue    粤语
wyw    文言文
jp    日语
kor    韩语
fra    法语
spa    西班牙语
th    泰语
ara    阿拉伯语
ru    俄语
pt    葡萄牙语
de    德语
it    意大利语
el    希腊语
nl    荷兰语
pl    波兰语
bul    保加利亚语
est    爱沙尼亚语
dan    丹麦语
fin    芬兰语
cs    捷克语
rom    罗马尼亚语
slo    斯洛文尼亚语
swe    瑞典语
hu    匈牙利语
cht    繁体中文
vie    越南语
'''


# 创建文件夹
def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


# 访问百度图片获取信息
def get_data(name, pn):
    keys = {
        'tn': 'baiduimage',
        'word': str(name),
        'pn': str(pn),  # 从0开始30的倍数
        'rn': '30',
    }
    baseurl = 'https://image.baidu.com/search/index'

    response = requests.get(baseurl, params=keys)

    return response
    # with open('a.html', 'wb')as f:
    #     f.write(response.content)


# 获取图片地址
def get_img_url(response):
    p = re.compile('"thumbURL":"(.*?jpg)"', re.S)
    urls = p.findall(str(response.text))
    print(urls)
    return urls


# 下载一张图片
def get_one_img(url, img_path, img_name):
    content = requests.get(url).content
    with open('{}/{}.jpg'.format(img_path, img_name), 'wb') as f:
        print(img_name + '下载成功')
        f.write(content)


# 获取某路径下某扩展名的详情信息(文件个数和文件名)
def get_file_count(path, type):
    """
    :param path: 文件夹路径
    :param type: 文件扩展名
    :return: 返回一个字典，counts表示文件个数，filenames表示所有文件的文件名
    """
    import os.path
    dir = path
    m = 0
    files = []
    for parentdir, dirname, filenames in os.walk(dir):
        for filename in filenames:
            # print(filename)
            files.append(filename)
            if os.path.splitext(filename)[1] == type:
                m = m + 1
    # print(m)
    return {'counts': m, 'filenames': files}


# 获取所需的图片
def get_needs_imgs(imgs_needs, img_type):
    tran_img_type = str(translate(img_type, 'en')).lower()  # 翻译完之后所有字母小写

    img_path = 'imgs/' + tran_img_type  # 图片存储路径
    mkdir(img_path)  # 创建文件夹

    img_pg = 0  # 30的倍数
    while True:
        files_details = get_file_count(img_path, '.jpg')  # 查看当前目录下已经有多少图片
        count = files_details['counts']  # 获取指定路径下有多少文件
        count2 = count
        if count2 >= imgs_needs:
            print('指定文件夹下已经有{}张图片了'.format(str(imgs_needs)))
            break
        res = get_data(img_type, img_pg)
        urls = get_img_url(res)
        for url in urls:
            try:
                get_one_img(url, img_path, tran_img_type + str(count2))
                count2 = count2 + 1
            except Exception as e:
                pass
            if count2 >= imgs_needs:
                break
        img_pg += 30


# 主要是为了多进程
def main(img_type):
    get_needs_imgs(imgs_needs=imgs_needs, img_type=img_type)


imgs_needs = 800  # 需要多少张图片
img_types = ['汽车','兔子','吉他','房子']  # 需要什么图片
# get_needs_imgs(imgs_needs, img_type)


if __name__ == '__main__':
    # 使用多进程
    pool = Pool()
    pool.map(main, img_types)
