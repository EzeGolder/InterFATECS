num = int(input())

for i in range(1, num + 1):
    if i % 4 == 0:
        print ("pim ", end=" ")
    else:
        print (f"{i} ", end= " ")

