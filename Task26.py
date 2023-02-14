""" Задача 26
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.

Пример:
A = 3; B = 5 -> 243 (3**5)
A = 2; B = 3 -> 8 """

def power(num, expon):
    
    if expon == 1:
        return num
    return num * power(num, expon - 1)


print(f'The result of exponentiation is {power(int(input("Enter a number: ")), int(input("Enter an exponenta: ")))}')

