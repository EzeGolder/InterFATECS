n = int(input())
atual = 0
anterior = 0
inicial = 0


for i in range(n):
    if i == 0:
        atual = int(input())
        if atual < 0:
            inicial = atual
        continue
    else:
        anterior = atual
        atual = int(input()) + anterior
        if atual < 0:
            if inicial > atual:
                inicial = atual


print(inicial * -1)

