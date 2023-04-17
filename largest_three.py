# wap for largest among three numbers

num1 = int(input(" Enter the first number : "))
num2 = int(input(" Enter the second number : "))
num3 = int(input(" Enter the third number : "))

if num1 > num2 and num1 > num3:
    print(" First Number is biggest ")
elif num2 > num1 and num2 > num3:
    print(" Second Number is biggest ")
elif num3 > num1 and num3 > num2:
    print(" Third Number is biggest ")
else:
    print(" All are same ")
