import math

chars = []
lines = []
soma_total = 0



saida = []
insert = True
while insert:
    chars = [char for char in input().split()]

    lines.append(chars)

    if len(chars) == 1 and chars[0] == '*':
        lines.append("*")
        insert = False



for i in range(len(lines) - 1):

    power = 0
    num = len(lines[i]) - 1
    while num >= 0:

        soma = 0
        for y in lines[i][num]:

            if y == '.':
                soma += 1
            elif y == '-':
                soma += 5
            else: soma = 0

        soma_total += soma * pow(20, power)

        power += 1
        num -= 1

    saida.append(soma_total)
    soma_total = 0


for s in saida:
    print(s)







