entrada1, volta1 = [int(n) for n in input().split()]
entrada2, volta2 = [int(n) for n in input().split()]

contador1 = entrada1
contador2 = entrada2
tempo = 0

while True:
    entrada1+= 1
    entrada2 +=1
    tempo += 1


    if entrada1 % volta1 == 0 and entrada2 % volta2 == 0:
        print(tempo)
        break

