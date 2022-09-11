# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

import math
pi = str(math.pi)
print (pi)

num = input("Введите точность вывода числа Пи: ")

result = ""
i=0
while i < len(num):
    result = result + pi[i]
    i+=1

print(result)
