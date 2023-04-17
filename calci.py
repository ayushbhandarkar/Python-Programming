# wap for calculator
import math


class Calculator:

    n1 = 0
    n2 = 1

    def get_two(self):
        self.n1 = int(input(" Enter the first number : "))
        self.n2 = int(input(" Enter the second number : "))

    def get_one(self):
        self.n1 = int(input(" Enter the number : "))

    def add(self):
        self.get_two()
        print(" Addition : ", self.n1 + self.n2)

    def sub(self):
        self.get_two()
        print(' Subtraction : ', self.n1 - self.n2)

    def mult(self):
        self.get_two()
        print(" Multiplication : ", self.n1 * self.n2)

    def div(self):
        self.get_two()
        print(" Division : ", self.n1 / self.n2)

    def square(self):
        self.get_one()
        print(" Square of ", self.n1, end=" : ")
        print(self.n1*self.n1)

    def sq_rt(self):
        self.get_one()
        print(" Square root of ", self.n1, end=" : ")
        print(math.sqrt(self.n1))


obj = Calculator()
sign = input(" Enter sign of operation ('+' , '-' , '*' , '/' , '%' , 'sq' , 'sqr') : ")

if sign == '+':
    obj.add()
elif sign == '-':
    obj.sub()
elif sign == '*':
    obj.mult()
elif sign == '/':
    obj.div()
elif sign == 'sq':
    obj.square()
elif sign == 'sqr':
    obj.sq_rt()
else:
    print(" Invalid Input! try again")
