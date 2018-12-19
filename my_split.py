# -*- coding: utf-8 -*-
# @Time    : 18-12-19 下午2:38
# @Author  : Felix Wang

import re


def my_split(string, sep=None, maxsplit=-1):
    if sep is None:
        string = re.sub('\\s+', ' ', string.strip())
        sep = ' '

    sep_len = len(sep)
    lists = []

    while True:
        if string.find(sep) == -1 or maxsplit == 0:
            lists.append(string)
            return lists
        else:
            index = string.find(sep)
            lists.append(string[:index])
            string = string[index + sep_len:]

            if maxsplit > 0:
                maxsplit -= 1


goal_str = 'dd\t d           \nd\r\d \t\nd dda '

print(my_split(goal_str, '\t', 10))  # 切割多少次
print(goal_str.split('\t', 10))
print(my_split(goal_str, 'd'))  # 不指定次数
print(goal_str.split('d'))
print(my_split(goal_str))  # 不指定次数格切割字符串
print(goal_str.split())
