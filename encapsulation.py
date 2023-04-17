class Car:

    def drive(self):
        print("Driving the car ")

    def __update_software(self):  # this method has been private
        print("Updating software")

    # def __init__(self):           # first way to access private method
        # self.__update_software()


volvo = Car()
volvo.drive()
volvo._Car__update_software()       # another way to access private method
