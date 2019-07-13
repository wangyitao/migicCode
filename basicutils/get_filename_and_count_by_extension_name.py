# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午10:02
# @Author  : Felix Wang
import os


def get_file_count(path, type):
    """
    :param path: 文件夹路径
    :param type: 文件扩展名
    :return: 返回一个字典，counts表示文件个数，filenames表示所有文件的文件名
    """
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


print(get_file_count('./', '.py'))
