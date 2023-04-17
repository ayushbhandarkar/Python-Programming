row = int(input(" Enter the number of rows : "))

for i in range(1, row+1):
    sp = row-i
    for j in range(sp):
        print(" ", end=" ")
    temp = i
    for j in range(temp, 0, -1):
        print(temp, end=" ")
        temp -= 1
    temp = i
    for j in range(1, temp):
        print(j+1, end=" ")
    print()
