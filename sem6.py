# Задача 1. Дано натуральное число N. Найдите значение выражения:
# N + NN + NNN
# N может быть любой длины.
# N = 132:132 + 132132 + 132132132 = 132264396

import random


def Sum():

    number = str(132)
    number2 = int(number)
    kount = 1
    sum = int(number)

    for i in range(len(number)):
        kount *= 10

    for i in range(2):
        number2 = number2*kount+int(number)
        sum += number2

    print(sum)


# Задача 2. Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число. Напишите программу,
# которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

def Similar():

    number = [random.randint(1, 9) for i in range(15)]
    print(number)

    print(f"Введите трехзначное натуральное число: ", end='')
    n = input()
    if len(n) < 3 or len(n) > 3 or not n.isnumeric():
        print("Вы ввели неверное число!")
        exit()
    n = int(n)

    for i in range(13):
        k = int(str(int(number[i])) + str(int(number[i+1]))+str(int((number[i+2]))))
        if k == n:
            print(number)
            print(f"{n} - да")
            exit()
        elif i == 12:
            print(f"{n} - нет")


# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def Zadacha():

    chislitel = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    znamenatel = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
    drobi=[]
    kount = 0

    for i in range(0,11):
        for k in range(1,11):
            kount = 0
            for j in range (2, chislitel[i]+1):
                if chislitel[i]%j == 0 and znamenatel[k]%j==0:
                    kount = 1
            if kount !=1 and chislitel[i]/znamenatel[k]<1:
                n=str(chislitel[i])+"/"+str(znamenatel[k])
                drobi.append(n)

    print(drobi) 


