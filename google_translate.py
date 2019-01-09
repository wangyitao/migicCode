# -*- coding: utf-8 -*-
# @Time    : 19-1-9 下午7:29
# @Author  : Felix Wang

import requests  # pip install requests
import execjs  # pip install PyExecJS  # 需要注意， 包的名称：PyExecJS


class GoogleTranslate(object):
    def __init__(self):
        self.ctx = execjs.compile(  # 下面是一段js代码，从网页中分析得到
            """ function TL(a) { var k = ""; var b = 406644; var b1 = 3293161072; var jd = "."; var $b = "+-a^+6"; var Zb = "+-3^+b+-f"; for (var e = [], f = 0, g = 0; g < a.length; g++) { var m = a.charCodeAt(g); 128 > m ? e[f++] = m : (2048 > m ? e[f++] = m >> 6 | 192 : (55296 == (m & 64512) && g + 1 < a.length && 56320 == (a.charCodeAt(g + 1) & 64512) ? (m = 65536 + ((m & 1023) << 10) + (a.charCodeAt(++g) & 1023), e[f++] = m >> 18 | 240, e[f++] = m >> 12 & 63 | 128) : e[f++] = m >> 12 | 224, e[f++] = m >> 6 & 63 | 128), e[f++] = m & 63 | 128) } a = b; for (f = 0; f < e.length; f++) a += e[f], a = RL(a, $b); a = RL(a, Zb); a ^= b1 || 0; 0 > a && (a = (a & 2147483647) + 2147483648); a %= 1E6; return a.toString() + jd + (a ^ b) }; function RL(a, b) { var t = "a"; var Yb = "+"; for (var c = 0; c < b.length - 2; c += 3) { var d = b.charAt(c + 2), d = d >= t ? d.charCodeAt(0) - 87 : Number(d), d = b.charAt(c + 1) == Yb ? a >>> d: a << d; a = b.charAt(c) == Yb ? a + d & 4294967295 : a ^ d } return a } """)

    def getTk(self, text):  # 计算谷歌的算法值
        return self.ctx.call("TL", text)

    def translate(self, content, en_to_zh=True):
        """
        :param content: 翻译内容
        :param en_to_zn: 是否由英文翻译成中文，默认为True
        :return:
        """
        if len(content) > 4891:
            print("翻译的长度超过限制！！！")
            return
        tk = self.getTk(content)
        param = {'tk': tk, 'q': content}
        url_zh_to_en = 'https://translate.google.cn/translate_a/single?client=t&sl=zh-CN&tl=en&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&otf=1&ssel=6&tsel=3&kc=1'
        url_en_to_zh = "https://translate.google.cn/translate_a/single?client=t&sl=en &tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss &dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1&srcrom=0&ssel=0&tsel=0&kc=2"

        # 返回的结果为Json，解析为一个嵌套列表
        result = requests.get(url_en_to_zh if en_to_zh else url_zh_to_en, params=param)
        results = result.json()[0]
        data = []
        for test in results:
            if test[0]:
                data.append(test[0])
        return '\n'.join(data), data


if __name__ == "__main__":
    tran = GoogleTranslate()  # 实例化谷歌翻译对象
    content = """Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"""
    # content = '你好啊,我今天去哪吃饭？你明天去哪？'
    data = tran.translate(content, en_to_zh=True)
    print(data[0])
