import math
import matplotlib.pyplot as plt
import Drawing


#треугольная функция
def triangle(coord, index):
    if coord <= 0 and index == 0:
        return 1
    if coord >= 100 and index == 9:
        return 1
    a = (-abs(coord - index * 10 - 5) + 10) / 10
    if a >= 0:
        return a
    else:
        return 0


#трапециевидная функция
def trapeze(coord, index):
    if coord <= 0 and index == 0:
        return 1
    if coord >= 100 and index == 9:
        return 1
    a = (-2 * abs(coord - index * 10 - 5) + 15) / 10
    if a >= 0:
        if a > 1:
            return 1
        else:
            return a
    else:
        return 0


#гауссова функция
def gaussian(coord, index, sigm=7):
    if coord <= 0 and index == 0:
        return 1
    if coord >= 100 and index == 9:
        return 1
    a = math.exp(-pow((coord - 10 * index - 5), 2) / sigm)
    if a < 0.00001:
        return 0
    return a


def buildGraphs():
    buildGraph(triangle, 'Triangle')
    buildGraph(trapeze, 'Trapeze')
    buildGraph(gaussian, 'Gaussian')

#график
def buildGraph(func, name):
    x_data = [0.1 * x for x in range(501)]
    print(x_data)
    for k in range(5):
        y_data = []
        for x in x_data:
            y_data.append(func(x, k))
        print(y_data)
        Drawing.drawGraph(name, x_data, y_data, index=k)
    Drawing.closeGraph()

