# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


n = int(input("Введите количество чисел последовательности: "))

list = []
list1 = []

for i in range(1, n + 1):
    x = randint(-10, 10)
    list.append(x)
print(list)

for i in list:
    if i not in list1:
        list1.append(i)
        
print(list1)