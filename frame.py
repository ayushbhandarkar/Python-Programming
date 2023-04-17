
def pattern(str):
    count = len(str)
    # code to find biggest string
    big = len(str[0])
    for i in range(1, count):
        if big < len(str[i]):
            big = len(str[i])
    # first line
    for i in range(0, big+5):
        print("*", end="")
    print()
    # mid string
    for i in range(0, count):
        length = len(str[i])+2
        f_length = (big+4)-length
        print("* " + str[i], end="")
        for j in range(0, f_length):
            print(" ", end="")
        print("*")
    # last line
    for i in range(0, big+5):
        print("*", end="")


stat = input(" Enter any string : ")
new_string = stat.split(" ")
pattern(new_string)


# for i in range(1, row+1):
#     for j in range(1, row+1):
#         if i == 1 or j == 1 or i == row or j == row:
#             print(" *", end=" ")
#         else:
#             print("  ", end=" ")
#     print()

