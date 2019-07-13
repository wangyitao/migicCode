import re
import time
import random
import requests
import execjs
import hashlib
import json

"""
功能
	翻译软件,支持:
		-百度翻译
		-有道翻译
		-谷歌翻译
作者:
	Ahab
公众号:
	Ahab杂货铺
User-Agent和Cookie 需要自行添加
"""
'''
Function:
	百度翻译类
'''


class BaiDu(object):
    def __init__(self):
        self.session = requests.Session()
        self.session.cookies.set('BAIDUID', '545B79DBBEA3414B7A4F2970A4AF24B6:FG=1;')
        self.session.cookies.set('PSTM', '%d;' % int(time.time()))
        User_Agent = [
            'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36',
            'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        ]
        self.headers = {
            'User-Agent': random.choice(User_Agent)
        }
        self.data = {
            'query': '',
            'sign': '',
            'token': '',
            'from': 'en',
            'to': 'zh',
        }
        self.url = 'https://fanyi.baidu.com/basetrans'

    def translate(self, word, en_to_zh=True):
        self.data['query'] = word
        self.data['token'], gtk = self.getTokenGtk()
        self.data['sign'] = self.getSign(gtk, word)
        if not en_to_zh:
            self.data['from'] = 'zh'
            self.data['to'] = 'en'
        res = self.session.post(self.url, data=self.data, headers=self.headers)
        return '\n'.join([i[1] for i in res.json()['trans'][0]['result']])

    def getTokenGtk(self, url='https://fanyi.baidu.com/'):
        res = self.session.get(url)
        token = re.compile(r"token:.*?'(.*?)'").search(res.text).group(1)
        gtk = re.findall(r";window.gtk = ('.*?');", res.text)[0]
        return token, gtk

    def getSign(self, gtk, word):
        js = r'''
        function a(r) {
                if (Array.isArray(r)) {
                    for (var o = 0, t = Array(r.length); o < r.length; o++)
                        t[o] = r[o];
                    return t
                }
                return Array.from(r)
            }
            function n(r, o) {
                for (var t = 0; t < o.length - 2; t += 3) {
                    var a = o.charAt(t + 2);
                    a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                        a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                        r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
                }
                return r
            }
            function e(r) {
                var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
                if (null === o) {
                    var t = r.length;
                    t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
                } else {
                    for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
                        "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                        C !== h - 1 && f.push(o[C]);
                    var g = f.length;
                    g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
                }
                var u = void 0
                    , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
                u = 'null !== i ? i : (i = window[l] || "") || ""';
                for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
                    var A = r.charCodeAt(v);
                    128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
                        S[c++] = A >> 18 | 240,
                        S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
                        S[c++] = A >> 6 & 63 | 128),
                        S[c++] = 63 & A | 128)
                }
                for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
                    p += S[b],
                        p = n(p, F);
                return p = n(p, D),
                    p ^= s,
                0 > p && (p = (2147483647 & p) + 2147483648),
                    p %= 1e6,
                p.toString() + "." + (p ^ m)
            }
        '''
        js = js.replace('\'null !== i ? i : (i = window[l] || "") || ""\'', gtk)
        sign = execjs.compile(js).call('e', word)
        return sign


#
# '''
# Function:
# 	有道翻译类
# '''
#
#
class YouDao():
    def __init__(self):
        self.headers = {
            # 'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
            'Referer': 'http://fanyi.youdao.com/',
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            'Cookie': 'OUTFOX_SEARCH_USER_ID=-1397887118@10.108.160.18;'
        }
        self.data = {
            'i': None,
            'client': 'fanyideskweb',
            'keyfrom': 'fanyi.web',
            'salt': '',
            'sign': '',
            'from': 'en',
            'to': 'zh',
        }
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    def translate(self, word, en_to_zh=True):
        datas = self.getsign(word)
        if not en_to_zh:
            self.data['from'] = 'zh'
            self.data['to'] = 'en'
        self.data['i'] = word
        self.data['salt'] = datas['salt']
        self.data['sign'] = hashlib.md5(datas['sign'].encode('utf8')).hexdigest()
        res = requests.post(self.url, headers=self.headers, data=self.data)
        return '\n'.join(res.json()['translateResult']).strip()

    def getsign(self, word):
        js_code = '''function sign(e){var r=""+(new Date).getTime(),i=r+parseInt(10*Math.random(),10);return{ts:r,salt:i,sign:"fanyideskweb"+e+i+"97_3(jkMYg@T[KZQmqjTK"}}'''
        sign = execjs.compile(js_code).call('sign', word)
        return sign


#
#
# '''
# Function:
# 	Google翻译类
# '''
#
#
class Google(object):
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
        return '\n'.join(data)


class Translate(object):
    def baidu(self, content, en_to_zh=True):
        baidutran = BaiDu()
        return baidutran.translate(content, en_to_zh)

    def youdao(self, content, en_to_zh=True):
        youdaotran = YouDao()
        return youdaotran.translate(content, en_to_zh)

    def google(self, content, en_to_zh=True):
        googletran = Google()
        return googletran.translate(content, en_to_zh)


if __name__ == '__main__':
    tran = Translate()
    print(tran.google('娱乐',en_to_zh=False))
    # content = '''
    # It's true that we don't know what we've got until we lose it, but it's also true that we don't know what we've been losing until it arrives.
    # '''
    # print(tran.baidu(content))
    # print(tran.google(content))
    # print(tran.youdao(content))
    #
    # content = """Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"""
    # print(tran.baidu(content))
    # print('\n')
    # print(tran.google(content))
    # print('\n')
    # print(tran.youdao(content))
    # print('\n')
    #
    # content = '''
    # 一个人至少拥有一个梦想，有一个理由去坚强。心若没有栖息的地方，到哪里都是在流浪。
    # '''
    # print(tran.baidu(content,en_to_zh=False))
    # print('\n')
    # print(tran.google(content,en_to_zh=False))
    # print('\n')
    # print(tran.youdao(content,en_to_zh=False))
    # print('\n')

