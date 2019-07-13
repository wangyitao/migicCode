# -*- coding: utf-8 -*-
# @Time    : 19-1-11 上午9:33
# @Author  : Felix Wang

import xlrd
from openpyxl import load_workbook
import openpyxl
from openpyxl.drawing.image import Image


class OperationExcel(object):
    def __init__(self, filename):
        self.filename = filename
        try:
            self.__workbook = xlrd.open_workbook(self.filename)
        except Exception as e:
            self.creatwb(self.filename)
            self.__workbook = xlrd.open_workbook(self.filename)
        self.__wb = load_workbook(self.filename)

    def get_sheet_names(self):

        return self.__wb.sheetnames

    def get_data(self, row=1, col=1, sheet_name=None, flag='0'):
        """
        :param sheet_name: 表名
        :param row: 行位置
        :param col: 列位置
        :param flag:标志，0：表示获取某行某列，1：获取某行，2：获取某列
        :return:返回
        """
        if sheet_name is None:
            sheet_name = self.get_sheet_names()[0]
        sheet = self.__workbook.sheet_by_name(sheet_name)
        # c = sheet.ncols  # 最大列数
        # w = sheet.nrows  # 最大行数
        # print(c, w)
        try:
            if str(flag) == '0':
                return sheet.row_values(row - 1)[col - 1]
            if str(flag) == '1':
                return sheet.row_values(row - 1)
            if str(flag) == '2':
                return sheet.col_values(col - 1)
        except Exception as e:
            print('该位置没有数据', e)

    def get_all_data(self, sheet_name=None):
        # if sheet_name is None:
        #     ws = self.__wb.active
        # else:
        #     ws = self.__wb.get_sheet_by_name(sheet_name)
        # # 获取表格所有行和列，两者都是可迭代的
        # rows = ws.rows
        # columns = ws.columns
        #
        # # 迭代所有的行
        # datas = []
        # for row in rows:
        #     line = [col.value for col in row]
        #     datas.append(line)
        #     print(line)
        #
        # return datas

        if sheet_name is None:
            sheet_name = self.get_sheet_names()[0]
        sheet = self.__workbook.sheet_by_name(sheet_name)
        datas = []
        data = []
        for i in range(sheet.nrows):
            data.append(sheet.row_values(i))
            # datas.append(data)
        return data

    def get_max_row_and_col(self):
        ws = self.__wb.active
        # sheet = self.__workbook.sheet_by_name(sheet_name)
        # return {'max_rows': sheet.nrows, 'max_cols': sheet.ncols}
        return {'max_rows': ws.max_row, 'max_cols': ws.max_column}

    # 新建excel
    def creatwb(self, filename):
        wb = openpyxl.Workbook()
        wb.save(filename=filename)
        print("新建Excel：" + filename + "成功")

    # 写入数据
    def write_data(self, col, row, data):
        ws = self.__wb.active
        # ws.cell(row=row, column=col).value = data
        ws.cell(row, col, data)
        self.__wb.save(self.filename)
        self.__wb.close()

    # 往Excel中插入图片
    def insert_img(self, img_name, place=None):
        ws = self.__wb.active
        img = Image(img_name)
        if place is None:
            ws.add_image(img)
        else:
            ws.add_image(img, place)  # 例如'A1'
        self.__wb.save(self.filename)
        self.__wb.close()


if __name__ == '__main__':
    op = OperationExcel('a.xlsx')
    d = op.get_sheet_names()
    print(d)
    # print(op.get_data('Sheet2', 1, 2, 0))
    # print(op.get_all_data('Sheet1'))
    op.write_data(1, 3, 'test')
    op.write_data(2, 3, 't2est')

    # op.insert_img(r'1234.jpg')
    # op.insert_img(r'1234.jpg', 'D3')


'''

　　####循环插入字典可以使用这种方法
row_and_col = op.get_max_row_and_col()
max_rows = row_and_col['max_rows']
max_cols = row_and_col['max_cols']
if max_rows == 1 and max_cols == 1:
    print('开始插入Excel标题')
    i = 1
    for key in data.keys():
        op.write_data( i, 1, key)
        op.write_data( i, 2, data[key])
        i += 1
    print('插入Excel标题成功')
if max_rows > 1 or max_cols > 1:
    print('开始插入Excel数据')
    j = 1
    for key in data.keys():
        op.write_data( j, max_rows + 1, data[key])
        j += 1
    print('插入Excel数据成功')
# 循环插入字典时
'''
