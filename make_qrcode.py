# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午10:13
# @Author  : Felix Wang

import qrcode
from PIL import Image


def make_qrcode(data, qrimg_path, logo_path=None):
    """
    生成二维码
    :param data: 网址
    :param qrimg_path: 二维码存放路径
    :param logo_path: logo路径，logo必须是png格式图片
    :return:
    """
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=8,
        border=2
    )
    qr.add_data(data)  # 添加信息
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert('RGBA')

    if logo_path:
        # 添加logo时logo的格式为png，不然会报错
        icon = Image.open(logo_path)
        img_w, img_h = img.size
        factor = 5  # 比例，过小可能无法识别
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size

        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        img.paste(icon, (w, h), icon)

    img.save(qrimg_path)


if __name__ == '__main__':
    test = """
    将进酒⑴
    书法作品《将进酒》
    书法作品《将进酒》(13张)
    君不见，黄河之水天上来⑵，奔流到海不复回。
    君不见，高堂明镜悲白发，朝如青丝暮成雪⑶。
    人生得意须尽欢⑷，莫使金樽空对月。
    天生我材必有用，千金散尽还复来。
    烹羊宰牛且为乐，会须一饮三百杯⑸。
    岑夫子，丹丘生⑹，将进酒，杯莫停⑺。
    与君歌一曲⑻，请君为我倾耳听⑼。
    钟鼓馔玉不足贵⑽，但愿长醉不复醒⑾。
    古来圣贤皆寂寞，惟有饮者留其名。
    陈王昔时宴平乐，斗酒十千恣欢谑⑿。
    主人何为言少钱⒀，径须沽取对君酌⒁。
    五花马⒂，千金裘，呼儿将出换美酒，与尔同销万古愁⒃。 [1]
    """

    url = 'www.baidu.com'

    make_qrcode(url,'url_qrcode.png')
    make_qrcode(test, 'test_qrcode.png')
    make_qrcode(test,'test_with_logo_qrcode.png',logo_path='logo.png') # logo必须是png
