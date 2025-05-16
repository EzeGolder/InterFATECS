import math
saida =[]
lines = []
while True:

    a, b, theta = [float(n) for n in input().split()]

    if a ==0 and b == 0 and theta ==0:
        break

    area = (a * b * math.sin(math.radians(theta))) / 2

    saida.append(area)


for s in saida:
    print(f"{s:.4f}")







