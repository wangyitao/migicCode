# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午9:44
# @Author  : Felix Wang

import re
import requests
from multiprocessing import Pool


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
    img_path = 'imgs/' + img_type  # 图片存储路径
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
                get_one_img(url, img_path, img_type + str(count2))
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
img_types = ['劳斯莱斯','波多野结衣']  # 需要什么图片
# get_needs_imgs(imgs_needs, img_type)


if __name__ == '__main__':
    # 使用多进程
    pool = Pool()
    pool.map(main, img_types)
