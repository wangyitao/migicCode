""" test 1 简单画图"""
# from matplotlib import pyplot as plt
#
# fig = plt.figure(figsize=(20, 8), dpi=80)  # figure图形图标的意思，这里是指我们画的图，figsize表示图像大小，dpi表示图片清晰度
# x = range(2, 26, 2)  # 数据在x轴的位置，是一个可迭代对象
#
# y = [15, 13, 14.5, 17, 20, 25, 26, 26, 27, 22, 18, 15]  # 数据在y轴的位置，是一个可迭代对象
# plt.plot(x, y)  # 传入x和y，通过plot绘制出折线图
#
# plt.xticks(x) # 设置x轴的刻度
# # plt.xticks(x[::2]) # 当刻度太密集的时候使用列表步长来解决，matplotlib自动帮我们对应
#
# # plt.savefig('./pic.png')  # 保存图片
# plt.show()  # 在执行程序的是否展示图形

""" test 2 自定义x轴标签，中文乱码解决，添加图例等"""
# # 使用 fc-list :lang=zh 查看中文字体
# # 指定字体的路径，然后在使用的时候使用fontproperties指定字体
#
# from matplotlib import pyplot as plt
# from matplotlib import font_manager
# import random
#
# my_font = font_manager.FontProperties(fname='/home/felix/.local/share/fonts/SIMHEI.TTF')  # 字体的路径
#
# plt.figure(figsize=(20, 8), dpi=80)
# x = range(120)
#
# random.seed(10)  # 设置随机种子，让不同时候随机得到的结果都相同
# y = [random.uniform(20, 35) for i in range(120)]  # 随机产生数据
# y2 = [random.uniform(20, 35) for i in range(120)]  # 随机产生数据
#
# plt.plot(x, y, label='10点到12点天气变化')  # 如果要添加图例则使用label指定图例名称
# plt.plot(x, y2, label='13点到14点天气变化')
# plt.legend(prop=my_font, loc='best')  # 图例通过prop指定字体，通过loc指定位置
#
# _x_ticks = ['10点{}分'.format(i) if i < 60 else '11点{}分'.format(i - 60) for i in x]  # 产生自定义的x轴数组
#
# # 将第一个参数的x的位置用第二个参数的数组一一对应显示，rotation表示旋转，fontproperties表示指定字体
# plt.xticks(x[::5], _x_ticks[::5], rotation=90, fontproperties=my_font)
# # 添加描述信息
# plt.xlabel('时间', fontproperties=my_font)  # 设置x轴的标签
# plt.ylabel('温度(℃)', fontproperties=my_font)  # 设置y轴的标签
# plt.title('10点到12点每分钟的时间变化情况', fontproperties=my_font)  # 设置title
#
# plt.grid(alpha=0.4,linestyle=':') # 绘制网格
# plt.show()

""" 常用统计图对比 """
# 折线图:以折线的上升或下降来表示统计数量的增减变化的统计图
# 特点:能够显示数据的变化趋势，反映事物的变化情况。(变化)
#
# 直方图:由一系列高度不等的纵向条纹或线段表示数据分布的情况。
# 一般用横轴表示数据范围，纵轴表示分布情况。
# 特点:绘制连续性的数据,展示一组或者多组数据的分布状况(统计)
#
# 条形图:排列在工作表的列或行中的数据可以绘制到条形图中。
# 特点:绘制连离散的数据,能够一眼看出各个数据的大小,比较数据之间的差别。(统计)
#
# 散点图:用两组数据构成多个坐标点，考察坐标点的分布,判断两变量
# 之间是否存在某种关联或总结坐标点的分布模式。
# 特点:判断变量之间是否存在数量关联趋势,展示离群点(分布规律)

""" test 3 散点图 """

# import random
# from matplotlib import (
#     pyplot as plt,
#     font_manager,
# )
#
# # 设置字体
# my_font = font_manager.FontProperties(fname='/home/felix/.local/share/fonts/SIMHEI.TTF')
#
# y_3 = [random.randint(8, 15) for i in range(31)]
# y_10 = [random.randint(10, 25) for j in range(31)]
#
# x_3 = range(1, 32)
# x_10 = range(51, 82)
#
# # 设置图形大小
# plt.figure(figsize=(20, 8), dpi=80)
#
# # 使用scatter绘制散点图
# plt.scatter(x_3, y_3, label="3月份")
# plt.scatter(x_10, y_10, label='10月份')
#
# # 调整x轴的刻度
# _x = list(x_3) + list(x_10)
# _xtick_labels = ['3月{}日'.format(i) for i in x_3]
# _xtick_labels += ['10月{}日'.format(i - 50) for i in x_10]
#
# plt.xticks(_x[::3], _xtick_labels[::3], fontproperties=my_font, rotation=45)
#
# # 添加图例
# plt.legend(prop=my_font, loc='upper left')
#
# # 添加描述信息
# plt.xlabel('时间', fontproperties=my_font)
# plt.ylabel('温度 单位(t)', fontproperties=my_font)
# plt.title('3月份和10月份的温度变化散点图', fontproperties=my_font)
#
# plt.show()


""" test 4 条形图1 """

# import random
# from matplotlib import (
#     pyplot as plt,
#     font_manager,
# )
#
# # 设置字体
# my_font = font_manager.FontProperties(fname='/home/felix/.local/share/fonts/SIMHEI.TTF')
#
# a = ['电影{}'.format(i) for i in range(30)]  # 电影名称
# b = [random.randint(10, 50) for i in range(30)]  # 电影票房
#
# # 设置图形大小
# plt.figure(figsize=(20, 8), dpi=80)
# # 绘制条形图
# plt.bar(range(len(a)), b, width=0.3)
# # 设置字符串到x轴
# plt.xticks(range(len(a)), a, fontproperties=my_font, rotation=45)  # x轴对应
# plt.savefig('电影统计.png')
# plt.show()

""" test 5 条形图2 """

# 绘制横着的条形图
# import random
# from matplotlib import (
#     pyplot as plt,
#     font_manager,
# )
#
# # 设置字体
# my_font = font_manager.FontProperties(fname='/home/felix/.local/share/fonts/SIMHEI.TTF')
#
# a = ['电影{}'.format(i) for i in range(30)]  # 电影名称
# b = [random.randint(10, 50) for i in range(30)]  # 电影票房
#
# # 设置图形大小
# plt.figure(figsize=(8, 20), dpi=80)
# # 绘制横着的条形图
# plt.barh(range(len(a)), b, height=0.3, color='orange')
# # 设置字符串到x轴
# plt.yticks(range(len(a)), a, fontproperties=my_font)  # x轴对应
# # 添加网格
# plt.grid(alpha=0.3)
#
# plt.savefig('电影统计.png')
# plt.show()

""" test 6 条形图3 """
# from matplotlib import (
#     pyplot as plt,
#     font_manager,
# )
#
# # 设置字体
# my_font = font_manager.FontProperties(fname='/home/felix/.local/share/fonts/SIMHEI.TTF')
#
# a = ['猩球崛起', '敦刻尔克', '蜘蛛侠', '战狼2']
# b_16 = [15746, 312, 4497, 319]
# b_15 = [12357, 156, 2045, 168]
# b_14 = [2358, 399, 2357, 362]
#
# bar_width = 0.1
# x_14 = list(range(len(a)))
# x_15 = [i + bar_width for i in x_14]
# x_16 = [i + bar_width for i in x_15]
#
# plt.figure(dpi=80)
#
# plt.barh(x_14, b_14, color='red', height=bar_width, label='9月14日')
# plt.barh(x_15, b_15, color='yellow', height=bar_width, label='9月15日')
# plt.barh(x_16, b_16, color='blue', height=bar_width, label='9月16日')
#
# plt.yticks(x_15, a, fontproperties=my_font)
# plt.legend(prop=my_font)  # 标签
# plt.show()

""" test 7 直方图1 """

# import random
# from matplotlib import (
#     pyplot as plt,
#     font_manager,
# )
#
# # 一般来说能够使用直方图的都是那些没有统计过的数据
#
# # 设置字体
# my_font = font_manager.FontProperties(fname='/home/felix/.local/share/fonts/SIMHEI.TTF')
#
# a = [random.randint(10, 100) for i in range(100)]
# # 直方图组数计算方式：将数据分组，当数据在100个以内时，按数据多少常分5-12组
# # 组距：指每个小组的两个端点的距离
# # 组数：极差/组距
# d = 5  # 组距
# num_bins = (max(a) - min(a)) // d  # 注意组距一定要被numbins整除，否则会不均匀
# print(num_bins)
#
# plt.hist(a, num_bins)
#
# # 设置x轴的刻度
# plt.xticks(range(min(a), max(a) + d, d))
# # 显示网格
# plt.grid()
# plt.show()


""" test 8 直方图2 """
# import random
# from matplotlib import (
#     pyplot as plt,
#     font_manager,
# )
#
# # 直方图应用场景
# # 1、用户的年龄分布状态
# # 2、一段时间内用户的点击次数的分布状态
# # 3、用户活跃时间分布状态
#
# # 绘制不同刻度的x轴的直方图
#
# interval = [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 60, 90]
# width = [5, 5, 5, 5, 5, 5, 5, 5, 5, 15, 30, 60]
# quantity = [random.randint(500, 9000) for i in range(len(interval))]
#
# plt.figure(figsize=(20, 8), dpi=80)
#
# plt.bar(range(len(quantity)), quantity, width=1)
#
# # 设置x轴的刻度
# _x = [i - 0.5 for i in range(len(quantity) + 1)]
# _xtick_labels = interval + [150]
# plt.xticks(_x, _xtick_labels)
# plt.grid()
#
# plt.show()
#
