import matplotlib.pyplot as plt
import math
import numpy as np

colors = ['c', 'm', 'r', 'b', 'g']

#настраиваем вывод
fig = plt.figure(figsize=(10, 10))
major_ticks = np.arange(0, 101, 10)
minor_ticks = np.arange(0, 101, 5)
ax = fig.add_subplot(1, 1, 1)
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)
# And a corresponding grid
ax.grid(which='minor', alpha=0)
ax.grid(which='major', alpha=1)

plt.grid(which='both')

#рисование стрелочек, упрощает подбор углов для таблицы
def drawAngle(angle, x, y, filename):
    arrow_len = 3
    print('X{} : Y{} || Angle: {}'.format(x, y, angle))
    plt.arrow(x, y, math.cos(angle*math.pi/180)*arrow_len, math.sin(angle*math.pi/180)*arrow_len, width=0.5)
    plt.savefig(filename)

#Отрисовка отрезка
def drawSegment(point1, point2, filename='circle.png'):
    x_data = [point1[0], point2[0]]
    y_data = [point1[1], point2[1]]
    #plt.figure(figsize=(10, 10))
    plt.plot(x_data, y_data, color='b')
    plt.savefig(filename)

#Отрисовка графика
def drawGraph(name, x_data, y_data, index=0):
    plt.figure(figsize=(24, 6), num=1)
    plt.xlabel('x', size=14)
    plt.ylabel('y', size=14)
    plt.plot(x_data, y_data, color=colors[index], linestyle='-', label=name + ' k = ' + str(index))
    plt.legend()
    plt.savefig(name + '.png', format='png')

#Закрываем файл
def closeGraph():
    plt.close()
