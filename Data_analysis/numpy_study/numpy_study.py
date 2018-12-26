# -*- coding: utf-8 -*-
# @Time    : 18-12-26 下午7:01
# @Author  : Felix Wang

""" test1 numpy入门和简单使用"""
#
# # numpy简介
# # 一个在Python中做科学计算的基础库，重在数值计算，也是大部分PYTHON科学计算库的基础库，多用于在大型、多维数组上执行数值运算
#
# import numpy as np
#
# # 创建数组
# # 下面的a，b，c效果相同
# a = np.array([1, 2, 3, 4, 5])
# b = np.array(range(1, 6))
# c = np.arange(1, 6)  # arange用法： arange([start,] stop[,step,],dtype=None)
#
# # 数组的类名：
# a = np.array([1, 2, 3, 4, 5, 6])
# print(type(a))  # <class 'numpy.ndarray'>
# print(a.dtype)  # int64
#
# # 指定创建的数组的数据类型
# a = np.array([1, 0, 1, 0], dtype=np.bool)
# print(a)  # [ True False  True False]
#
# # 修改数组的数据类型
# a = a.astype(np.int8)
# print(a)  # [1 0 1 0]
#
# # 修改浮点型的小数位数
# b = np.round(a, 2)  # 将浮点数保留两位
# print(b)
#
# print('#' * 15)
#
# c = np.array([[3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9]])
# print(c)
#
# # 查看数组的形状
# print(c.shape)  # (2, 6)
# d = c.reshape(3, 4)
# # [[3 4 5 6]
# #  [7 8 4 5]
# #  [6 7 8 9]]
# print(d)
# print(d.shape)  # (3, 4)
#
# # 把数组转化为1维数组
# e = d.flatten()
# print(e)  # [3 4 5 6 7 8 4 5 6 7 8 9]
# # 注意 下面这个不是转换为一维数组
# ee = d.reshape(1, 12)
# print(ee)  # [[3 4 5 6 7 8 4 5 6 7 8 9]]
#
# # 加减乘除法
# # 注意：加减乘除在运算过程中，值被作用到所有的元素上
# print('#' * 15)
# print(d)
# # [[3 4 5 6]
# #  [7 8 4 5]
# #  [6 7 8 9]]
# print(d + 1)
# # [[ 4  5  6  7]
# #  [ 8  9  5  6]
# #  [ 7  8  9 10]]
# print(d * 2)
# # [[ 6  8 10 12]
# #  [14 16  8 10]
# #  [12 14 16 18]]
# print('#' * 15)
#
# #######################################
# a = np.array([[3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9]])
# b = np.array([[21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 31, 32]])
# # 数组和数组的加减法,对应的各个值相加减，或者相乘除
# print(a + b)
# # [[24 26 28 30 32 34]
# #  [31 33 35 37 39 41]]
# print(a * b)
# # [[ 63  88 115 144 175 208]
# #  [108 140 174 210 248 288]]
#
# # c = a.reshape(3, 4)  # 注意不同的维度的不能相乘除
# # print(a * c)
# # 但是：
# # 2行6列的数组,和1行6列的数组
# a = np.array([[3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9]])
# c = np.array([1, 2, 3, 4, 5, 6])
# print(a-c)
# # [[2 2 2 2 2 2]
# #  [3 3 3 3 3 3]]
# print(a*c)
# # [[ 3  8 15 24 35 48]
# #  [ 4 10 18 28 40 54]]
#
# # 2行6列的数组,和2行一列的数组
# a = np.array([[3, 4, 5, 6, 7, 8], [4, 5, 6, 7, 8, 9]])
# c=np.array([[1],[2]])
# print(c+a)
# # [[ 4  5  6  7  8  9]
# #  [ 6  7  8  9 10 11]]
# print(c*a)
# # [[ 3  4  5  6  7  8]
# #  [ 8 10 12 14 16 18]]
# # 造成上面这种不同维度能计算的原因是：
# # 如果两个数组的后缘长度，即从末尾开始算起的维度的轴长度相符或其中一方的长度为1，则认为他们是广播兼容的。广播会在缺失和长度为1的维度上进行
#

""" test2 numpy读取文件 """

# import numpy as np
#
# # numpy读取数据方法
# # np.loadtxt(fname,dtype=np.float,delimiter=None,skiprows=0,usecols=None,unpack=False)
# # frame: 文件、字符串或产生器，可以是.gz或bz2压缩文件
# # dtype： 数据类型，可选，CSV的字符串以什么数据类型读入数组中，默认np.float
# # delimiter: 分隔字符串，默认是任何空格，改为逗号
# # skiprows： 跳过前x行，一般跳过第一行表头
# # usecols： 读取指定的列，索引，元组类型
# # unpack： 如果为True，读入属性将分为写入不同数组变量，False读入数据只写入一个数组变量，默认False
#
#
# us_file_path = "US_video_data_numbers.csv"
# uk_file_path = "GB_video_data_numbers.csv"
#
# # t1 = np.loadtxt(us_file_path,delimiter=",",dtype="int",unpack=True)
# t2 = np.loadtxt(us_file_path, delimiter=",", dtype="int")
#
# # print(t1)
# print(t2)
#
# print("*" * 100)
#
# # 取行
# # print(t2[2])
#
# # 取连续的多行
# # print(t2[2:])
#
# # 取不连续的多行
# # print(t2[[2,8,10]])
#
# # print(t2[1,:])
# # print(t2[2:,:])
# # print(t2[[2,10,3],:])
#
# # 取列
# # print(t2[:,0])
#
# # 取连续的多列
# # print(t2[:,2:])
#
# # 取不连续的多列
# # print(t2[:,[0,2]])
#
# # 去行和列，取第3行，第四列的值
# # a = t2[2,3]
# # print(a)
# # print(type(a))
#
# # 取多行和多列，取第3行到第五行，第2列到第4列的结果
# # 去的是行和列交叉点的位置
# b = t2[2:5, 1:4]
# # print(b)
#
# # 取多个不相邻的点
# # 选出来的结果是（0，0） （2，1） （2，3）
# c = t2[[0, 2, 2], [0, 1, 3]]
# print(c)


""" test3 numpy中的其他操作"""
# import numpy as np
#
# # 求转置的三种方法
# b = np.array([[1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9]])
# print(b)
# print(b.T)
# print(b.swapaxes(1, 0))
# print(b.transpose())
#
# # numpy中的三目运算符
# c = np.where(b < 5, 10, 0)  # 如果b中的数字小于5，则至10，否则置0
# print(c)
#
# # 小于x替换为x，大于y替换为y
# bb = np.array(
#     [[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11], [12, 13, 14, 15, 16, 17], [18, 19, 20, np.nan, np.nan, np.nan]])
# print(bb)
# cc = bb.clip(10, 18)
# print(cc)

""" test4 numpy中的nan和inf """
# # nan： 表示不是一个数字
# #     当我们读取本地文件为float的时候，如果有缺失，就会出现nan
# #     或者做了一个不合适的计算的时候。
#
# # inf：表示正无穷，-inf表示负无穷
# #     比如：一个数字除以0（python中直接会报错，numpy中是一个inf或者-inf）
# import numpy as np
#
# a = np.nan
# b = np.inf
# print(a, type(a))  # nan <class 'float'>
# print(b, type(b))  # inf <class 'float'>
#
# # numpy中的nan的注意点
# # 1、两个nan是不相等的
# # 2、np.nan!=np.nan
# # 3、利用2的特性判断数组中nan的个数 # np.count_nonzero(t!=t)
# # 4、使用np.isnan(a)来判断一个数组中是否是nan，比如希望把nan替换为0，t[np.isnan(t)]=0
# # 5、nan和任何值计算都为nan
#
# # 在一组数据中如果单纯的把nan替换为0，是不合适的，比如全部替换为0后，替换之前的平均值如果大于0，替换之后的均值肯定会变小，所以更一般的方式是把缺失的数字替换为均值(中值)
# # 或者是直接删除有缺失值的一行
# """ 将nan替换为均值的方法
# def fill_ndarray(t1):
#     for i in range(t1.shape[1]):  # 遍历每一列
#         temp_col = t1[:, i]  # 当前的一列
#         nan_num = np.count_nonzero(temp_col != temp_col)
#         if nan_num != 0:  # 不为0，说明当前这一列中有nan
#             temp_not_nan_col = temp_col[temp_col == temp_col]  # 当前一列不为nan的array
#
#             # 选中当前为nan的位置，把值赋值为不为nan的均值
#             temp_col[np.isnan(temp_col)] = temp_not_nan_col.mean()
#     return t1
#
#
# if __name__ == '__main__':
#     t1 = np.arange(24).reshape((4, 6)).astype("float")
#     t1[1, 2:] = np.nan
#     print(t1)
#     t1 = fill_ndarray(t1)
#     print(t1)
# """
#
# # numpy中常用统计函数
# # 求和：t.sum(axis=None)
# # 均值：t.mean(a,axis=None)  受离群点的影响较大
# # 中值：np.median(t,axis=None)
# # 最大值：t.max(axis=None)
# # 最小值：t.min(axis=None)
# # 极值：np.ptp(t,axis=None) 即最大值和最小值之差
# # 标准差：t.std(axis=None)
#
#
# # 数组的拼接，注意：竖直拼接的时候，每一列代表的意义要相同，否则牛头不对马嘴
# t1 = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
# t2 = np.array([[12, 13, 14, 15, 16, 17], [18, 19, 20, 21, 22, 23]])
# tt1 = np.vstack((t1, t2))  # 竖直拼接
# tt2 = np.hstack((t1, t2))
# print(tt1)
# # [[ 0  1  2  3  4  5]
# #  [ 6  7  8  9 10 11]
# #  [12 13 14 15 16 17]
# #  [18 19 20 21 22 23]]
# print(tt2)
# # [[ 0  1  2  3  4  5 12 13 14 15 16 17]
# #  [ 6  7  8  9 10 11 18 19 20 21 22 23]]
#
# # 数组的行列交换
# print(tt1)
# tt1[[1, 2], :] = tt1[[2, 1], :]  # 行交换
# print(tt1)
# tt1[:, [0, 2]] = tt1[:, [2, 0]]  # 列交换
# print(tt1)


""" test5 更多其他方法 """
# import numpy as np
#
# # 1、获得最大值最小值的位置
# #     # np.argmax(t,axis=0)
# #     # np.argmin(t,axis=1)
# # 2、创建全为0的数组： np.zeros((3,4))
# # 3、创建全为1的数组： np.ones((3,4))
# # 4、创建一个对角线为1的正方形数组(方阵)：np.eye(3)
#
# # numpy生成随机数
# # print(np.random.rand(4,2,3)) # 创建均匀分布的的随机数数组，浮点数，范围：0-1
# # print(np.random.rand(1,2))
#
# print(np.random.randn(2, 2))  # 创建标准正态分布随机数，浮点数，平均数0，标准差1
#
# print(np.random.randint(1, 10, (3, 4)))  # 从给定上下限范围选取随机整数,最后一个参数为形状
#
# print(np.random.uniform(1, 10, (3, 4)))  # 产生具有均匀分布的数组，第一个参数为起始值，第二个参数为结束值，第三个参数为形状
#
# print(np.random.normal(1, 1, (3, 4)))  # 从指定正态分布中随机抽取样本，分布中心是第一个参数（均值），标准差为第二个值，第三个参数为形状
#
# print(np.random.seed(10))  # 随机数中值，可以通过设置相同的种子，使没吃生成的随机数相同
