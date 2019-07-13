# -*- coding: utf-8 -*-
# @Time    : 19-1-6 上午10:57
# @Author  : Felix Wang

import requests
import random
import hashlib


def get_pic(size=256):
    styles = ['identicon', 'monsterid', 'wavatar']
    random_str = ''.join([chr(random.randint(0x0000, 0x9fbf)) for i in range(random.randint(1, 25))])

    m1 = hashlib.md5("{}".format(random_str).encode("utf-8")).hexdigest()
    url = 'http://www.gravatar.com/avatar/{}?s={}&d={}'.format(m1, size, random.choice(styles))
    res = requests.get(url)
    with open('image.jpg', 'wb')as f:
        f.write(res.content)


get_pic()
