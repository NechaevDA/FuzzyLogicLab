import MemFunctions
import Drawing
import math
import random


#таблица углов
direction_table =[
    [315, 315, 315, 290, 290, 290, 290, 280, 240, 225],
    [330, 330, 340, 345, 350, 350, 330, 290, 240, 225],
    [ 10,  20,  25,  20,  10, 350, 330, 315, 270, 225],
    [ 20,  60,  60,  45,  30, 355, 315, 290, 255, 200],
    [ 20,  80,  80,  85,  85, 355, 300, 280, 260, 200],
    [ 20,  80, 100, 120, 175, 265, 265, 260, 260, 200],
    [ 20,  75, 110, 135, 175, 210, 225, 240, 240, 200],
    [ 45,  70, 115, 150, 170, 190, 200, 205, 210, 190],
    [ 45,  60, 110, 150, 170, 170, 165, 160, 150, 150],
    [ 45,  60, 100, 110, 110, 110, 110, 135, 135, 135],
]



def getNextPoint(point, angle, step):
    next_x = point[0] + math.cos(angle*math.pi/180)*step
    next_y = point[1] + math.sin(angle*math.pi/180)*step
    return next_x, next_y

def getAngle(coefficients, direction_angles):
    print(direction_angles)
    print(coefficients)
    avg = direction_angles[0]
    #Нормируем углы, чтобы они находились в одной половине
    for i in range(1, len(direction_angles)):
        if avg - direction_angles[i] >= 180:
            direction_angles[i] += 360
        elif direction_angles[i] - avg >= 180:
            direction_angles[i] -= 360
        avg = (avg/i + direction_angles[i]) / (i+1)
    print(direction_angles)

    weighted_angle = 0
    weighted_coefficients = 0

    #По формуле получаем сумму углов и коеффициентов
    for i in range(len(direction_angles)):
        weighted_angle += direction_angles[i]*coefficients[i]
        weighted_coefficients += coefficients[i]
    weighted_angle /= weighted_coefficients
    print(weighted_angle)
    return weighted_angle


def fuzzyCircle(start_x, start_y, step_len, function, number_of_steps):
    x = start_x
    y = start_y
    for i in range(number_of_steps):
        direction_angles = []
        coefficients = []
        # Вычисляем индексы полос, к которым принадлежит текущая позиция, запоминаем угол в том квадрате и
        # коэффициент принадлежности
        for i in range(10):
            for j in range(10):
                if (function(y, i) and function(x, j)):
                    angle = direction_table[9-i][j]
                    print('I: {} J: {} A: {}'.format(9-i, j, angle))
                    direction_angles.append(angle) #Запоминаем угол
                    coefficients.append(function(y, i)*function(x, j)) #Запоминаем коэффициент
        #Вычисляем угол в текущей точке
        angle = getAngle(coefficients, direction_angles)
        #Получаем координаты следующей точки
        next_point = getNextPoint((x, y), angle, step_len)
        Drawing.drawSegment((x, y), next_point)
        print(next_point)
        x = next_point[0]
        y = next_point[1]


def main():
    #for i in range(1, 9):
    #    for j in range(1, 9):
    #        direction_table[i][j] = random.randint(0, 360)

    #for i in range(9, -1, -1):
    #    for j in range(10):
    #        y = 95 - i*10
    #        x = j*10 + 5
    #        Drawing.drawAngle(direction_table[i][j], x, y, 'angles.png')
    #Drawing.closeGraph()
    """
    Первые два параметра - начальная точка
    Третий - длина шага
    Четвертый - функция принадлежности
    Пятый - количество шагов
    :return:
    """
    fuzzyCircle(50, 50, 1, MemFunctions.triangle, 400)
    Drawing.closeGraph()





main()
