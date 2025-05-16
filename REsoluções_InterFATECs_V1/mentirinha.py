import math
num = int(input())

contador = 0
for i in range(1, num + 1):
    if num % i == 0 :
        contador += 1


if contador == 3:
    print("sim")
else:
    print("nao")




