""" Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
а некоторые – гербом. Определите минимальное число монеток, которые нужно 
перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть """

import random

def ListCreation(num):
    list1 = []
    for i in range(num):
        list1.append(random.randint(0,1))
    print(list1)
    return list1

def CalculationsAndResult(list):
    sum = 0
    for i in range(len(list)):
        sum += list[i]
    if (len(list) - sum) < sum:
        print("Flip ", (len(list)-sum), "coins")
    else:
        print("Flip ", sum, "coins")
    
coins = int(input('Input coins: '))
CalculationsAndResult(ListCreation(coins))