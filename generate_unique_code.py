# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午9:36
# @Author  : Felix Wang

import uuid
from hashlib import md5
import datetime
import random


def my_id_maker():
    return md5(str('{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()) + ''.join(
        [str(random.randint(1, 10)) for i in range(5)])).encode('utf8') + str(uuid.uuid1()).encode('utf8')).hexdigest()

    # 简单版本的下面就行了
    # return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now()) + ''.join(
    #     [str(random.randint(1, 10)) for i in range(5)])


print(my_id_maker())
