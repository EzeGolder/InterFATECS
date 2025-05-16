q = int(input())
saida = []

for _ in range (q):
    num1 = int(input())
    num2 = int(input())

    if num1 > num2 and num1 + num2 > 40:
        saida.append("DOROTHY DECIDE E A NONNA VAI")
    elif num1 > num2 and num1 + num2 <= 40:
        saida.append("DOROTHY DECIDE")
    elif num1 < num2 and num1 + num2 > 40:
        saida.append("DAGMAR DECIDE E A NONNA VAI")
    elif num1 < num2 and  num1 + num2 <= 40:
        saida.append("DAGMAR DECIDE")



for s in saida:
    print(s)