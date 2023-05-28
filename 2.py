""" Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), 
а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа. """

import random
import math

def Calculations():
    X = random.randint(1, 1000)
    Y = random.randint(1, 1000)
    print(X, Y)
# S = int(input("Input sum: "))
    S = X+Y
# P = int(input("Input prod: "))
    P = X*Y
# y*y - S*y + P = 0
    D = S*S - 4*P
# y = (--S+-sqrt(D))/2
    if D < 0:
        print("No solution")
    elif D == 0:
        print(-S/2)
    else:
        print(int((S+math.sqrt(D))/2), int((S-math.sqrt(D))/2))

Calculations()
