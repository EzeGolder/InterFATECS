import math

n, theta, something = [int(n) for n in input().split()]

rot = [[math.cos(math.radians(theta)), -math.sin(math.radians(theta)) ], [math.sin(math.radians(theta)), math.cos(math.radians(theta))]]

saida = []
for _ in range(n):
    x, y = [int(n) for n in input().split()]

    xl = rot[0][0] * x + rot[0][1] * y
    yl = rot[1][0] * x + rot[1][1] * y
    saida.append(f"{xl:.2f} {yl:.2f}")

for s in saida:
    print(s)


