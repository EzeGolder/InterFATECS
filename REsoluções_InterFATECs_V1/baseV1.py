entrada1, volta1 = [int(n) for n in input().split()]
entrada2, volta2 = [int(n) for n in input().split()]

contador1 = entrada1
contador2 = entrada2
tempo = 0

while True:
    tempo += 1
    contador1 +=1
    contador2 +=1

    if contador1 == volta1:
        contador1 = 0

    if contador2 == volta2:
        contador2 = 0

    if contador1 == 0 and contador2 == 0:
        print(tempo)
        break

