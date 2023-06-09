'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
*Пример:*
A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 '''
a = int(input("Введите число: "))
b = int(input("Введите степень числа: "))

def power(a, b):
    if (b == 1):
        return a
    return a * power(a, b - 1)

print(f"Число {a} в степени {b} = {power(a, b)}")

'''Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух 
целых неотрицательных чисел. Из всех арифметических операций допускаются 
только +1 и -1. Также нельзя использовать циклы.
*Пример:*
2 2 = 4 '''
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

def recurSum(a, b):
    if a == 0:
        return b
    else:
        return recurSum(a - 1, b + 1)

print(f"Сумма чисел {a} и {b} = {recurSum(a, b)}")