# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午9:39
# @Author  : Felix Wang

# pip install pypinyin
from pypinyin import pinyin, lazy_pinyin, Style, load_phrases_dict, load_single_dict
from pypinyin.style import register

print(pinyin('你好'))  # [['nǐ'], ['hǎo']]
print(pinyin('中心', heteronym=True))  # 启用多音字模式  # [['zhōng', 'zhòng'], ['xīn']]
print(pinyin('中心', style=Style.FIRST_LETTER))  # 设置拼音风格，第一个字母 [['z'], ['x']]
print(pinyin('中心', style=Style.TONE2, heteronym=True))  # [['zho1ng', 'zho4ng'], ['xi1n']]
print(lazy_pinyin('中心'))  # 不考虑多音字的情况 # ['zhong', 'xin']

##########处理不包含拼音的字符
# default (默认行为): 不做任何处理，原样返回:
print(lazy_pinyin('你好☆☆'))  # ['ni', 'hao', '☆☆']
# ignore : 忽略该字符
print(lazy_pinyin('你好☆☆', errors='ignore'))  # ['ni', 'hao']
# replace : 替换为去掉 \u 的 unicode 编码
print(lazy_pinyin('你好☆☆', errors='replace'))  # ['ni', 'hao', '26062606']
# callable 对象 : 提供一个回调函数，接受无拼音字符(串)作为参数, 支持的返回值类型: unicode 或 list ([unicode, …]) 或 None 。
print(lazy_pinyin('你好☆☆', errors=lambda x: 'star'))  # ['ni', 'hao', 'star']

########### 自定义拼音库
print(lazy_pinyin('还没', style=Style.TONE2))
load_phrases_dict({'桔子': [['jú'], ['zǐ']]})  # 增加 "桔子" 词组，可以自己定义
print(lazy_pinyin('桔子', style=Style.TONE2))

load_single_dict({ord('还'): 'hái,huán'})  # 调整 "还" 字的拼音顺序
print(lazy_pinyin('还没', style=Style.TONE2))


###########自定义拼音风格
@register('kiss')
def kiss(mypinyin, **kwargs):
    return '😘 {0}'.format(mypinyin)


print(lazy_pinyin('么么哒', style='kiss'))
