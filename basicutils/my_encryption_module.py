# -*- coding: utf-8 -*-
# @Time    : 19-1-11 上午9:43
# @Author  : Felix Wang

from hashlib import md5, sha1, sha512


def encryption(data):
    flag = bytes('@#$%', encoding='utf8')
    if type(data) == type(str()):
        byte = flag + bytes(data, encoding='utf8') + flag
    # print(str(byte,'utf8'))
    elif type(data) == type(bytes()):
        byte = flag + data + flag
    else:
        raise TypeError('data must be str or bytes')

    return md5(byte).hexdigest()


def str_encrypt(data):
    """
    使用sha1加密算法，返回str加密后的字符串
    """
    flag = bytes('@#$%', encoding='utf8')
    if type(data) == type(str()):
        byte = flag + bytes(data, encoding='utf8') + flag
    # print(str(byte,'utf8'))
    elif type(data) == type(bytes()):
        byte = flag + data + flag
    else:
        raise TypeError('data must be str or bytes')

    sha = sha1(byte).hexdigest()
    sha5 = sha512(bytes(sha, encoding='utf8')).hexdigest()

    return encryption(sha5)


print(str_encrypt('你好'))
print(str_encrypt(bytes('你好', encoding='utf8')))
print(str_encrypt(open('logo.png', 'rb').read()))
