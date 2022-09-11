# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

number = int(input("Введите число натуральной степени: "))
size = number + 1
numbers = []
for i in range(size):
    numbers.append(random.randint(0,101))

step = []
for i in range(0, number+1):
    step.append(i)

list = []
for i in range(size):
    list.append(str(numbers[i])+"*x**"+str(step[i]))

temp_str = ""
i=len(list)-1

while i >= 0:
    temp_str += list[i]+"+"
    i-=1

left_str = temp_str[:-1]

right_str = "=0"

result = left_str + right_str
print(result)

data = open("txt_for_zad4.txt", "w")
data.writelines(result)
data.close()