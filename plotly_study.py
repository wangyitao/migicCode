# -*- coding: utf-8 -*-
# @Time    : 19-1-11 上午10:28
# @Author  : Felix Wang

import plotly.plotly as plt
import plotly.offline as pltoff  # pip install plotly
from plotly.graph_objs import *

# 生成折线图
def line_plots(name):
    dataset = {'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
               'y': [5, 4, 1, 3, 11, 2, 6, 7, 19, 20],
               'z': [12, 9, 0, 0, 3, 25, 8, 17, 22, 5]}

    data_g = []

    tr_x = Scatter(
        x=dataset['x'],
        y=dataset['y'],
        name='y'
    )
    data_g.append(tr_x)

    tr_z = Scatter(
        x=dataset['x'],
        y=dataset['z'],
        name='z'
    )
    data_g.append(tr_z)

    layout = Layout(title="line plots", xaxis={'title': 'x'}, yaxis={'title': 'value'})
    fig = Figure(data=data_g, layout=layout)
    pltoff.plot(fig, filename=name)


# 生成散点图
def scatter_plots(name):
    dataset = {'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
               'y': [5, 4, 1, 3, 11, 2, 6, 7, 19, 20],
               'text': ['5_txt', '4_txt', '1_txt', '3_txt', '11_txt', '2_txt', '6_txt', '7_txt', '19_txt', '20_txt']}

    data_g = []

    tr_x = Scatter(
        x=dataset['x'],
        y=dataset['y'],
        text=dataset['text'],
        textposition='top center',
        mode='markers+text',
        name='y'
    )
    data_g.append(tr_x)

    layout = Layout(title="scatter plots", xaxis={'title': 'x'}, yaxis={'title': 'value'})
    fig = Figure(data=data_g, layout=layout)
    pltoff.plot(fig, filename=name)


# 生成柱状图
def bar_charts(name):
    dataset = {'x': ['Windows', 'Linux', 'Unix', 'MacOS'],
               'y1': [45, 26, 37, 13],
               'y2': [19, 27, 33, 21]}
    data_g = []
    tr_y1 = Bar(
        x=dataset['x'],
        y=dataset['y1'],
        name='v1'
    )
    data_g.append(tr_y1)

    tr_y2 = Bar(
        x=dataset['x'],
        y=dataset['y2'],
        name='v2'
    )
    data_g.append(tr_y2)
    layout = Layout(title="bar charts", xaxis={'title': 'x'}, yaxis={'title': 'value'})
    fig = Figure(data=data_g, layout=layout)
    pltoff.plot(fig, filename=name)


# 生成饼图
def pie_charts(name):
    dataset = {'labels': ['Windows', 'Linux', 'Unix', 'MacOS', 'Android', 'iOS'],
               'values': [280, 25, 10, 100, 250, 270]}
    data_g = []
    tr_p = Pie(
        labels=dataset['labels'],
        values=dataset['values']
    )
    data_g.append(tr_p)
    layout = Layout(title="pie charts")
    fig = Figure(data=data_g, layout=layout)
    pltoff.plot(fig, filename=name)


# 充满区域的图
def filled_area_plots(name):
    dataset = {'x': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
               'y1': [5, 4, 1, 3, 11, 2, 6, 7, 19, 20],
               'y2': [12, 9, 0, 0, 3, 25, 8, 17, 22, 5],
               'y3': [13, 22, 46, 1, 15, 4, 18, 11, 17, 20]}

    dataset['y1_stack'] = dataset['y1']
    dataset['y2_stack'] = [y1 + y2 for y1, y2 in zip(dataset['y1'], dataset['y2'])]
    dataset['y3_stack'] = [y1 + y2 + y3 for y1, y2, y3 in zip(dataset['y1'], dataset['y2'], dataset['y3'])]

    dataset['y1_text'] = ['%s(%s%%)' % (y1, y1 * 100 / y3_s) for y1, y3_s in zip(dataset['y1'], dataset['y3_stack'])]
    dataset['y2_text'] = ['%s(%s%%)' % (y2, y2 * 100 / y3_s) for y2, y3_s in zip(dataset['y2'], dataset['y3_stack'])]
    dataset['y3_text'] = ['%s(%s%%)' % (y3, y3 * 100 / y3_s) for y3, y3_s in zip(dataset['y3'], dataset['y3_stack'])]

    data_g = []
    tr_1 = Scatter(
        x=dataset['x'],
        y=dataset['y1_stack'],
        text=dataset['y1_text'],
        hoverinfo='x+text',
        mode='lines',
        name='y1',
        fill='tozeroy'
    )
    data_g.append(tr_1)

    tr_2 = Scatter(
        x=dataset['x'],
        y=dataset['y2_stack'],
        text=dataset['y2_text'],
        hoverinfo='x+text',
        mode='lines',
        name='y2',
        fill='tonexty'
    )
    data_g.append(tr_2)

    tr_3 = Scatter(
        x=dataset['x'],
        y=dataset['y3_stack'],
        text=dataset['y3_text'],
        hoverinfo='x+text',
        mode='lines',
        name='y3',
        fill='tonexty'
    )
    data_g.append(tr_3)

    layout = Layout(title="filled area plots", xaxis={'title': 'x'}, yaxis={'title': 'value'})
    fig = Figure(data=data_g, layout=layout)
    pltoff.plot(fig, filename=name)


if __name__ == '__main__':
    name = 'test4.html'
    # line_plots(name)
    scatter_plots(name)
    # bar_charts(name)
    # pie_charts(name)
    # filled_area_plots(name)
