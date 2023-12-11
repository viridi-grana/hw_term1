from areas import *
from combinatorics import *

if __name__ == '__main__':

    answer = input('Каким модулем Вы хотите воспользоваться? Если Вас интересует модуль "Геометрия", нажмите 1. Если Вас интересует модуль "Комбинаторика", нажмите 2.\n')

    if answer == '1':
        func_you_need = input('Если Вам необходимо посчитать площадь треугольника, нажмите 1, площадь квадрата - нажмите 2, площадь прямоугольника - нажмите 3.\n')
        print(func_you_need)

        if func_you_need == '1':
            print(triangle)
        elif func_you_need == '2':
            print(square)
        elif func_you_need == '3':
            print(rectangle)

    else:
        func_you_need_2 = input('Если Вам необходимо посчитать факториал, то нажмите 1. Если необходима формула количества перестановок, также нажмите 1, если Вы интересуетесь формулой количества сочетаний, то нажмите 2, если Вам необходима формула количества размещений, нажмите 3.\n')

        if func_you_need_2 == '1':
            print(fact)
        elif func_you_need == '2':
            print(sochetanie)
        elif func_you_need == '3':
            print(razmeshenie)