# Задача 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и выводит название этого дня недели.

"""
a = int(input('Введите цифру дня недели: '))

b = ['Понедельник', 'Вторник', 'Среда', 'Четверг', ' Пятница', 'Суббота', 'Воскресенье']

if a < 1 or a > 7:
    print('Вы ввели не существующий день недели!')
else:
    print(b[a-1])

"""

# Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

"""

import math

x1 = float(input('Введите х координату первой точки: '))
y1 = float(input('Введите y координату первой точки: '))
x2 = float(input('Введите х координату второй точки: '))
y2 = float(input('Введите y координату второй точки: '))

ax = x1 - x2
ay = y1-y2
dlina = math.sqrt (ax**2 + ay**2)

print(dlina)

"""

# Задача 3. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

"""
a = int(input('Введите номер четверти: '))

b = ['x > 0, y > 0', 'x < 0, y > 0', 'x < 0, y < 0', 'x > 0, y < 0']

if a < 1 or a > 4:
    print('Вы ввели не правильный номер четверти!')
else:
    print(b[a-1])

"""

# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.

"""
a = int(input('Введите число N: '))

for i in range (1, a+1):
    if i % 2 == 0:
        print(i)

"""
