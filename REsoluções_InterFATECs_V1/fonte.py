tempo = int(input())
nivel1 = int(input())
nivel2 = int(input())
nivel3 = int(input())

total_nivel1 =0
total_nivel2 =0
total_nivel3 =0

total_nivel1 =( nivel2 * tempo )+ nivel3 * tempo * 2

total_nivel2 =(nivel1 * tempo)+ nivel3 * tempo

total_nivel3 = (nivel1 * tempo * 2) + nivel2 * tempo

if total_nivel1 < total_nivel2 and total_nivel1 < total_nivel3:
    print(2 * total_nivel1)
elif total_nivel2 < total_nivel3 and total_nivel2 < total_nivel1:
    print(2 *total_nivel2)
else:
    print( 2* total_nivel3)



