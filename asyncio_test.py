# -*- coding: utf-8 -*-
# @Time    : 19-1-8 下午3:41
# @Author  : Felix Wang

import asyncio
import time
import aiohttp
from pyquery.pyquery import PyQuery as pq


# async def add(x=1, y=2):
#     print('Add {} + {} ...'.format(x, y))
#     await asyncio.sleep(2)
#     return x + y
#
#
# s = time.time()
# loop = asyncio.get_event_loop()
# tasks = [loop.create_task(add(x, y)) for x, y in zip(range(1, 10), range(11, 20))]
# loop.run_until_complete(asyncio.wait(tasks))
# for t in tasks:
#     print(t.result())
# print('cost:', time.time() - s)


#
def decode_html(html_content):
    doc = pq(html_content)
    des = ''
    for li in doc.items('#phrsListTab .trans-container ul li'):
        des += li.text()
    return des


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main(words):
    urls = ['http://dict.youdao.com/w/eng/{}'.format(word) for word in words]
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            tasks.append(fetch(session, url))
        htmls = await asyncio.gather(*tasks)
        for html_content in htmls:
            print(decode_html(html_content))


if __name__ == '__main__':
    s = time.time()
    test = 'orange'
    words = test.split()
    words = words * 100
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(words))
    print(time.time() - s)
