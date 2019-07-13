# -*- coding: utf-8 -*-
# @Time    : 19-1-10 下午7:59
# @Author  : Felix Wang

import jieba  # pip install jieba
from scipy.misc import imread  # 这是一个处理图像的函数 pip install scipy
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator  # pip install wordcloud
import matplotlib.pyplot as plt  # pip install matplotlib


# 该函数的作用就是把屏蔽词去掉，使用这个函数就不用在WordCloud参数中添加stopwords参数了
# 把你需要屏蔽的词全部放入一个stopwords文本文件里即可
def stop_words(texts, stopwords=None):
    """
    停止词处理
    :param texts: 文本内容
    :param stopwords: 停止词路径
    :return:
    """
    words_list = []
    word_generator = jieba.cut(texts, cut_all=False)  # 返回的是一个迭代器
    if stopwords:
        with open(stopwords) as f:
            str_text = f.read()
            unicode_text = str(str_text)  # 把str格式转成unicode格式
            f.close()  # stopwords文本中词的格式是'一词一行'
    else:
        unicode_text = ''
    for word in word_generator:
        if word.strip() not in unicode_text:
            words_list.append(word)
    return ' '.join(words_list)  # 注意是空格


def get_img(base_img_path, goal_img_path, text_path, stopwords_path=None):
    """
    获得词云图片
    :param base_img_path: 词云基准图片
    :param goal_img_path: 输出目标图片
    :param text_path: 文本路径
    :param stopwords_path: 停止词路径
    :return:
    """
    back_color = imread(base_img_path)  # 解析该图片

    wc = WordCloud(background_color='white',  # 背景颜色
                   max_words=1000,  # 最大词数
                   mask=back_color,  # 以该参数值作图绘制词云，这个参数不为空时，width和height会被忽略
                   max_font_size=100,  # 显示字体的最大值
                   font_path="/home/felix/.local/share/fonts/SIMHEI.TTF",  # 解决显示口字型乱码问题，可使用查看 fc-list :lang=zh
                   random_state=42,  # 为每个词返回一个PIL颜色
                   # width=1000,  # 图片的宽
                   # height=860  #图片的长

                   )
    # WordCloud各含义参数请点击 wordcloud参数

    # 添加自己的词库分词，比如添加'金三胖'到jieba词库后，当你处理的文本中含有金三胖这个词，
    # 就会直接将'金三胖'当作一个词，而不会得到'金三'或'三胖'这样的词
    # jieba.add_word('金三胖')

    # 打开词源的文本文件
    with open(text_path) as f:
        text = stop_words(f.read(), stopwords_path)
        wc.generate(text)
    # 基于彩色图像生成相应彩色
    image_colors = ImageColorGenerator(back_color)
    # 显示图片
    plt.imshow(wc)
    # 关闭坐标轴
    plt.axis('off')
    # 绘制词云
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis('off')
    # 保存图片
    wc.to_file(goal_img_path)


get_img('base.jpg', 'word_cloud.jpg', 'news.txt')  # 不指定停止词
get_img('base.jpg', 'word_cloud.jpg', 'news.txt', stopwords_path='stopwords.txt')  # 指定停止词
