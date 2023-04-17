# write a program to swap program to swap two variables by using third variables

num1 = int(input(" Enter the first number : "))
num2 = int(input(" Enter the second number : "))

print(" Before swap : num1 = ", num1, end=" ")
print(" num2 = ", num2)

num3 = num1
num1 = num2
num2 = num3

print(" After swap : num1 = ", num1, end=" ")
print(" num2 = ", num2)


