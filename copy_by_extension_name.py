# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午9:30
# @Author  : Felix Wang


import os
import shutil


def cp_and_move_to(exts, fromdir, todir, is_all=True):
    """
    移动fromdir目录下所有扩展名为exts的文件到todir
    :param exts: 可以是列表或者字符串，如果是字符串，用空格分隔
    :param fromdir: 原目录 # 目录建议使用绝对路径
    :param todir: 目标目录，如果不存在，则建立
    :param is_all: 如果设置为False，直接拷贝全部，不考虑扩展名
    :return:
    """
    extss = []
    if type(exts) == str:
        extss = exts.lower().split()
    elif type(exts) == list:
        extss = exts
    fp = {}
    for root, dirs, files in os.walk(fromdir):
        for fl in files:
            if not is_all:  # 如果指定了扩展名
                if os.path.splitext(fl.lower())[1][1:] in extss:
                    fp.setdefault(root, []).append(fl)
            else:
                fp.setdefault(root, []).append(fl)
    for k, v in fp.items():
        relativepath = k[len(fromdir) + 1:]
        newpath = os.path.join(todir, relativepath)
        for f in v:
            oldfile = os.path.join(k, f)
            print("Copying [" + oldfile + "] To [" + newpath + "]")
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            shutil.copy(oldfile, newpath)


cp_and_move_to(['py', 'txt'], r'./', r'./my_dir/')
# cp_and_move_to('py txt', r'./', r'./dirr/')
