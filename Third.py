# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
import random

number=int(input("Введите размер последовательности: "))
list = []
for i in range(number):
    list.append(random.randint(10,99))

print(list)

i = 0
k = 1
while i < len(list):
    test = list[i]
    while k < len(list):
        if test == list[k]:
            # print(f" test[{test}] == list[k][{list[k]}]")
            list.pop(k)
            # k+=1
        elif test != list[k]:
            # print(f" test[{test}] != list[k][{list[k]}]")
            k+=1
    i+=1
    k=i+1

print(list)