# -*- coding: utf-8 -*-
# @Time    : 19-1-11 上午9:49
# @Author  : Felix Wang

import random
from io import BytesIO
# 首先要安装PIL库  pip3 install pillow
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def mkdir(path):
    # 引入模块
    import os
    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)
        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print(path + ' 目录已存在')
        return False


class CheckCode:
    def __init__(self, font_file, font_size=36, width=240, height=60, char_length=4, start_color_num=0,
                 end_color_num=255, is_simple=True, is_oncache=False):
        """
        初始化
        :param font_file: 字体文件
        :param font_size: 字体大小，默认36
        :param width: 验证码宽度
        :param height: 验证码高度
        :param char_length: 验证码文字个数
        :param start_color_num: 颜色开始的颜色
        :param end_color_num: 颜色结束
        :param is_simple: 是否是简体中文，默认为True，如果为False则可能包含繁体中文
        :param is_oncache: 是否存在缓存中，默认为False，表示以图片方式存储
        """
        self.is_oncache = is_oncache
        self.is_simple = is_simple
        self.font_file = font_file
        self.font_size = font_size
        self.width = width
        self.height = height
        self.char_length = char_length
        self.start_num = start_color_num
        self.end_num = end_color_num
        # 定义使用Image类实例化一个长为120px,宽为30px,基于RGB的(255,255,255)颜色的图片
        self.image = Image.new('RGB', (self.width, self.height), (255, 255, 255))
        # 创建Font对象:
        self.font = ImageFont.truetype(self.font_file, self.font_size)
        # 创建Draw对象:
        self.draw = ImageDraw.Draw(self.image)
        # 双下划綫的变量在类中不能直接访问起到保护的作用
        self.__code_text = []

    def get_random_code(self, time=1):
        """
        :param is_simple: 是否包含中文繁体字，默认不包含，True表示不包含
        :param time: 返回多少个
        :return: 返回一个随机字符列表
        """
        is_simple = self.is_simple
        codes = []
        for i in range(time):
            num = chr(random.randint(0x30, 0x39))  # 随机生成数字
            lowercase = chr(random.randint(0x61, 0x74))  # 随机生成小写字母
            capcase = chr(random.randint(0x41, 0x5a))  # 随机生成大写字母

            # Unicode编码的汉字，带繁体字 ，共2万多字
            zh = chr(random.randint(0x4e00, 0x9fbf))

            # gbk编码的简单汉字，无繁体字
            head = random.randint(0xb0, 0xf7)
            body = random.randint(0xa1, 0xf9)  # 在head区号为55的那一块最后5个汉字是乱码,为了方便缩减下范围
            val = f'{head:x}{body:x}'
            ch = bytes.fromhex(val).decode('gb2312')

            if is_simple:
                # code = random.choice([ch, num, lowercase, capcase])
                code = random.choice([ch, num, lowercase, capcase])
            else:
                code = random.choice([zh, num, lowercase, capcase])
            codes.append(code)
        return codes

    # 随机颜色:
    def rndColor(self, start, end, randomflag=True):
        """
        :param start:
        :param end:
        :param randomflag: 是否返回随机参数，
        :return:
        """
        return (random.randint(start, end), random.randint(start, end),
                random.randint(start, end))

    def rotate(self):
        self.image.rotate(random.randint(0, 90), expand=0)

    # 随机点
    def randPoint(self):
        return (random.randint(0, self.width), random.randint(0, self.height))

    # 随机线
    def randLine(self, num):
        draw = ImageDraw.Draw(self.image)
        for i in range(0, num):
            draw.line([self.randPoint(), self.randPoint()], self.rndColor(0, 255))
        del draw

    # 获取验证码
    def get_codes(self):
        return self.__code_text

    def draw_pic(self):
        # 填充每个像素:
        # 单一背景
        color = self.rndColor(170, 255)  # 可以把背景调浅色
        for x in range(self.width):
            for y in range(self.height):
                self.draw.point((x, y), fill=color)

        # 输出文字:
        codes = self.get_random_code(time=self.char_length)
        self.__code_text = []
        for ii in range(self.char_length):
            code = self.get_random_code()[0]
            self.__code_text.append(code)
            self.draw.text([random.randint(int((self.width / 2 - self.font_size / 2) / self.char_length * 2 * ii),
                                           int((self.width / 2 - self.font_size / 2) / self.char_length * 2 * (
                                                   ii + 1))), random.randint(0, self.height / 4)],
                           code, font=self.font, fill=self.rndColor(0, 120))  # 把字体调深色
        # self.rotate()

        # 画出随机线
        self.randLine(10)

        # 模糊:
        # self.image = self.image.filter(ImageFilter.BLUR)

        if self.is_oncache:  # 保存在缓存
            f = BytesIO()
            self.image.save(f, 'jpeg')
            return f.getvalue()
        else:
            # 保存
            self.image.save('images/{}.jpg'.format(''.join(self.get_codes())), 'jpeg')


# 创建文件夹，用来存放验证码
mkdir('images')

# 这里的字体采用能识别中文的字体
font_file = '/home/felix/.local/share/fonts/SIMHEI.TTF'
# checkcode = CheckCode(font_file=font_file, is_simple=True, char_length=random.randint(3, 7))

# 生成多张验证码
for i in range(100):
    checkcode = CheckCode(font_file=font_file, is_simple=True, char_length=random.randint(3, 7))
    checkcode.draw_pic()
    # 生成的验证码的内容
    codes = checkcode.get_codes()
    print(i, codes)
