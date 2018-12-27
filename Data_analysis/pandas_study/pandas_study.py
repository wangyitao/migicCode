# -*- coding: utf-8 -*-
# @Time    : 18-12-27 下午2:51
# @Author  : Felix Wang

""" test1 pandas简单操作 """
# # pandas 常用数据
# # 1、 Series 一维，带标签数组
# # 2、 DataFrame 二维，Series容器
#
# import numpy as np
# import pandas as pd
# import string
#
# # 创建Series方式一：
# t = pd.Series(np.arange(10), index=list(string.ascii_uppercase[:10]))
# print(t)
# print(type(t)) # <class 'pandas.core.series.Series'>
#
# # 创建Series方式二
# a = {string.ascii_uppercase[i]:i for i in range(10)}
# b = pd.Series(a)
# print(a)
# print(b)
# c = pd.Series(a,index=list(string.ascii_uppercase[5:15]))
# # 注意：重新给其指定其他的索引之后，如果能够对应上，就取其值，如果不能就为nan，因为nan为float类型，pandas会自动改变dtype
# print(c)
#
# # pandas的索引和切片
# print(c[2:10:2])
# print(c[1])
# print(c[c>4])
#
# print(b['A'])
# print(b[[2,3,6]])
#
# # Series的索引和值
# print(b.index)
# print(b.values)
# # 注：Series对象的本质上是由两个数组构成
# # 一个数组构成对象的键(index,索引)，一个数组构成对象的值(values)。键->值。

""" test2 pandas读取数据 """
# import pandas as pd
#
# #pandas读取csv中的文件
# df = pd.read_csv("./dogNames2.csv")
# df2 = pd.read_sql()
# df3 = pd.read_excel()
# df4 = pd.read_json()

""" test3 DataFrame对象 """
# import string
# import pandas as pd
# import numpy as np
#
# t = pd.DataFrame(np.arange(12).reshape((3, 4)))
# #    0  1   2   3
# # 0  0  1   2   3
# # 1  4  5   6   7
# # 2  8  9  10  11
# print(t)
#
# # DataFrame对象既有行索引，又有列索引
# # 行索引，表明不同行，横向索引，叫index，0轴，axis=0
# # 列索引，表名不同列，纵向索引，叫columns，1轴，axis=1
#
# t2 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list(string.ascii_uppercase[:3]),
#                   columns=list(string.ascii_uppercase[-4:]))
# #    W  X   Y   Z
# # A  0  1   2   3
# # B  4  5   6   7
# # C  8  9  10  11
# print(t2)
#
# # DataFrame的基础属性
# # df.shape # 行数，列数
# # df.dtypes # 列数据类型
# # df.ndim  # 数据维度
# # df.index # 行索引
# # df.columns # 列索引
# # df.values # 对象值，二维ndarray数组
#
# # # DataFrame整体情况查询
# # df.head(3) # 显示头部几行，默认5行
# # df.tail(3) # 显示末尾几行，默认5行
# # df.info() # 相关信息概览：行数，列数，列索引，列非空值个数，列类型，内存占用
# # df.describe() # 快速综合统计结果：计数，均值，标准差，最大值，四分位数，最小值
#
# # 排序
# ## 按值排序
# # df.sort_values(by, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
# # #### 参数说明
# # axis:{0 or ‘index’, 1 or ‘columns’}, default 0，默认按照索引排序，即纵向排序，如果为1，则是横向排序
# # by:str or list of str；如果axis=0，那么by="列名"；如果axis=1，那么by="行名"；
# # ascending:布尔型，True则升序，可以是[True,False]，即第一字段升序，第二个降序
# # inplace:布尔型，是否用排序后的数据框替换现有的数据框
# # kind:排序方法，{‘quicksort’, ‘mergesort’, ‘heapsort’}, default ‘quicksort’。似乎不用太关心
# # na_position : {‘first’, ‘last’}, default ‘last’，默认缺失值排在最后面
#
#
# # # pandas 之loc和iloc
# # # 1、df.loc 通过标签索引行数据
# # # 2、df.iloc 通过位置获取行数据
# # print('*' * 30)
# # print(t2)
# #
# # print(t2.loc['A', 'W'])  # 0
# # print(t2.loc[['A', 'C'], ['W', 'Z']])  # 选择间隔的多行多列
# # print(t2.loc['A':'C', ['W', 'Z']])  # 冒号是闭合的可以渠道冒号后面的值
# #
# # print(t2.iloc[1, 2])  # 6
# # print(t2.iloc[1:3, 0:3])
# #
# # # 赋值更改数据
# # print('*'*50)
# # print(t2)
# # t2.loc['A','W']=100
# # print(t2)
# # t2.iloc[1:2,0:3]=0
# # print(t2)
# #
# # # pandas的布尔索引
# # print(t2[t2['W']==0])
#
#
# # pandas之字符串方法归纳
# # cat ： 实现元素级的字符串连接操作，可指定分隔符
# # contains ： 返回表示各字符串是否含有指定模式的布尔型数组
# # count ： 模式的出现次数
# # endswith,startswith ： 相当于对各个元素执行x.endswith()或x.startswith()
# # findall ： 计算各字符串的模式列表
# # get ： 获取个元素的第i个字符
# # join ： 根据指定的分隔符将Series中各元素的字符串连接起来
# # len ： 计算各字符串的长度
# # lower,upper ： 转换大小写，相当于对各个元素执行x.lower或者x.upper
# # match ： 根据指定的正则表达式对各个元素执行re.match
# # pad : 在字符串的左边、右边或者左右两边添加空白
# # center ： 相当于pad(side='both')
# # repeat : 重复值。例如，s.str.repeat(3)相当于各个字符串执行x*3
# # replace ： 用指定字符串替换找到的模式
# # slice ： 对Series中的各个字符串进行子串截取
# # split ： 根据分隔符或者正则表达式对字符串进行拆分
# # strip,lstrip,rstrip ： 去除空白，包括换行符
#
# # 缺失数据的处理
# # 1、判断数据是否为NaN： pd.isnull(df),pd.notnull(df)
# # 2、处理方式
# # (1)、删除NaN所在的行列  t.dropna(axis=0,how='any',inplace=False)
# # (2)、填充数据，t.fillna(t.mean()),t.fillna(t.median()),t.fillna(0)
#
# # 数据合并之join
# t3 = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list(string.ascii_uppercase[:3]),
#                   columns=list(string.ascii_uppercase[-4:]))
# t4 = pd.DataFrame(np.arange(12).reshape((2, 6)), index=list(string.ascii_uppercase[:2]),
#                   columns=list(string.ascii_uppercase[-10:-4]))
#
# print(t3)
# print(t4)
# print(t3.join(t4))
# #    W  X   Y   Z    Q    R    S    T     U     V
# # A  0  1   2   3  0.0  1.0  2.0  3.0   4.0   5.0
# # B  4  5   6   7  6.0  7.0  8.0  9.0  10.0  11.0
# # C  8  9  10  11  NaN  NaN  NaN  NaN   NaN   NaN
#
#
# # 数据合并值merge
# # merge:按照指定的列把数据按照一定的方式合并到一起
# print('*' * 30)
# print(t3.merge(t4, left_on='Z', right_on='V'))  # left_on=right_on# 就相当于前面这个和后面这个相等的地方进行合并,默认how为inner
# #    W  X   Y   Z  Q  R  S  T   U   V
# # 0  8  9  10  11  6  7  8  9  10  11
#
# print(t3.merge(t4, left_on='Z', right_on='V', how='outer'))  # 交集，通过nan补全
# #      W    X     Y     Z    Q    R    S    T     U     V
# # 0  0.0  1.0   2.0   3.0  NaN  NaN  NaN  NaN   NaN   NaN
# # 1  4.0  5.0   6.0   7.0  NaN  NaN  NaN  NaN   NaN   NaN
# # 2  8.0  9.0  10.0  11.0  6.0  7.0  8.0  9.0  10.0  11.0
# # 3  NaN  NaN   NaN   NaN  0.0  1.0  2.0  3.0   4.0   5.0
#
# print(t3.merge(t4, left_on='Z', right_on='V', how='left'))  # 左边为准，通过nan补全
# #    W  X   Y   Z    Q    R    S    T     U     V
# # 0  0  1   2   3  NaN  NaN  NaN  NaN   NaN   NaN
# # 1  4  5   6   7  NaN  NaN  NaN  NaN   NaN   NaN
# # 2  8  9  10  11  6.0  7.0  8.0  9.0  10.0  11.0
# print(t3.merge(t4, left_on='Z', right_on='V', how='right'))  # 右边为准，通过nan补全
# #      W    X     Y     Z  Q  R  S  T   U   V
# # 0  8.0  9.0  10.0  11.0  6  7  8  9  10  11
# # 1  NaN  NaN   NaN   NaN  0  1  2  3   4   5
#
#
# # 分组和聚合
# # grouped = df.groupby(by="columns_name")
# # grouped是一个DataFrameGroupBy对象，是可迭代的
# # grouped中的每一个元素是一个元组
# # 元组里面是（索引(分组的值)，分组之后的DataFrame）
#
# # DataFrameGroupBy对象有很多经过优化的方法
# # count : 很注重非NAN值的数量
# # sum ： 非NA值的和
# # mean ： 非NA值的平均值
# # median ： 非NA值的算数中位数
# # std,var : 无偏标准差和方差
# # min,max ： 非NA值的最小值和最大值

""" test4 pandas其他知识点 """
import numpy as np
import pandas as pd

# 生成一段时间序列
print(pd.date_range(start='20180105', end='20180206', freq='D'))
# DatetimeIndex(['2018-01-05', '2018-01-06', '2018-01-07', '2018-01-08',
#                '2018-01-09', '2018-01-10', '2018-01-11', '2018-01-12',
#                '2018-01-13', '2018-01-14', '2018-01-15', '2018-01-16',
#                '2018-01-17', '2018-01-18', '2018-01-19', '2018-01-20',
#                '2018-01-21', '2018-01-22', '2018-01-23', '2018-01-24',
#                '2018-01-25', '2018-01-26', '2018-01-27', '2018-01-28',
#                '2018-01-29', '2018-01-30', '2018-01-31', '2018-02-01',
#                '2018-02-02', '2018-02-03', '2018-02-04', '2018-02-05',
#                '2018-02-06'],
#               dtype='datetime64[ns]', freq='D')

# 其中频率的更多缩写
# D   日历日
# B   每工作日
# H   每小时
# T   每分钟
# S   每秒
# L   每毫秒
# U   每微妙
# M   每月最后一个日历日
# BM  每月最后一个工作日
# MS  每月第一个日历日
# BMS 每月第一个工作日


# index = pd.date_range(start='20180102', periods=10)  # periods表示周期
# # 在DataFrame中使用时间序列
# df = pd.DataFrame(index, range(10), columns=['w'])
#
# # t4 = pd.DataFrame(np.arange(12).reshape((2, 6)), index=list(string.ascii_uppercase[:2]),
# #                   columns=list(string.ascii_uppercase[-10:-4]))
# print(df)
#
# # 把时间戳转换为DataFrame格式
# # df["timeStamp"] = pd.to_datetime(df["timeStamp"],format="")
# # print()
# #
# # format参数大部分情况下可以不用写，但是对于pandas无法格式化的时间字符串，我们可以使用该参数，比如包含中文
#
#
# # pandas重采样
# # 重采样： 指的是将时间序列从一个频率转化为另一个频率进行处理的过程，将高频率数据转化为低频率数据为降采样，低频率转化为高频率为升采样
# tt = pd.DataFrame(np.random.uniform(10,50,(100,1)),index=pd.date_range(start='20180508',periods=100))
# print(tt)
# print(tt.resample('M').mean())
# print(tt.resample('10D').count())


""" test5 北京pm2.5处理实例"""
# coding=utf-8
import pandas as pd
from matplotlib import pyplot as plt

file_path = "BeijingPM20100101_20151231.csv"

df = pd.read_csv(file_path)

# 把分开的时间字符串通过periodIndex的方法转化为pandas的时间类型
period = pd.PeriodIndex(year=df["year"], month=df["month"], day=df["day"], hour=df["hour"], freq="H")
df["datetime"] = period
# print(df.head(10))

# 把datetime 设置为索引
df.set_index("datetime", inplace=True)

# 进行降采样
df = df.resample("7D").mean()
print(df.head())
# 处理缺失数据，删除缺失数据
# print(df["PM_US Post"])

data = df["PM_US Post"]
data_china = df["PM_Nongzhanguan"]

print(data_china.head(100))
# 画图
_x = data.index
_x = [i.strftime("%Y%m%d") for i in _x]
_x_china = [i.strftime("%Y%m%d") for i in data_china.index]
print(len(_x_china), len(_x_china))
_y = data.values
_y_china = data_china.values

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x)), _y, label="US_POST", alpha=0.7)
plt.plot(range(len(_x_china)), _y_china, label="CN_POST", alpha=0.7)

plt.xticks(range(0, len(_x_china), 10), list(_x_china)[::10], rotation=45)

plt.legend(loc="best")

plt.show()
