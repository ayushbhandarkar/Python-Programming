students = [("Squidward", 'F', 60),
            ("Sandy", 'A', 40),
            ("Patrick", "D", 33),
            ("Spongebob", "B", 36),
            ("Mr. Crabs", "C", 85)]


# grade = lambda grades: grades[1]
# students.sort(key=grade)                     # sorting elements in ascending order using second index value
# print("Sorted elements using second index value : ", end="")
# for i in students:
#     print(i, end="")


age = lambda ages: ages[2]
students.sort(key=age, reverse=True)            # sorting elements in descending order using third index value
print("")
print("Sorted elements in ascending order using third index value : ")
print("")
for i in students:
    print(i)
