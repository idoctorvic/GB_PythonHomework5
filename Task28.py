""" Задача 28
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
неотрицательных чисел.
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.

Пример:
2 4
2 """

def Rec_sum(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    #summa = a
    a = Rec_sum(a, b - 1) + 1
    return a

a = int(input('1: '))
b = int(input('2: '))

print(f'The sum of {a} and {b} is {Rec_sum(a, b)}')