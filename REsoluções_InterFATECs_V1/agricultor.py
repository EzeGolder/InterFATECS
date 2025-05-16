sensores = int(input())

saida = []
for _ in range ( sensores):
    t, u, p = [float(n) for n in input().split()]

    if p == 1:
        saida.append("NAO REGAR")
    elif p == 0:
        if t > 30 and u < 50:
            saida.append("REGAR")
        else:
            saida.append("NAO REGAR")

for s in saida:
    print(s)

