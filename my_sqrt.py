# -*- coding: utf-8 -*-
# @Time    : 18-12-19 上午10:46
# @Author  : Felix Wang


def my_sqrt(num, accuracy=20):
    """
    :param num: 需要求根的书
    :param accuracy:  精度
    :return: 根的近似值
    """
    if num < 0:
        return -1
    else:
        start = 1
        diff = start * start - num
        while diff > 10 ** (-accuracy) or diff < -(10 ** (-accuracy)):
            diff2 = diff
            start = (start + num / start) / 2.0
            diff = start * start - num
            if diff2 == diff: break
        return start
