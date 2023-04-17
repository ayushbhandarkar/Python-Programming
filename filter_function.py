people = [("Mike", 17),
          ("Amol", 19),
          ("Monica", 16),
          ("Joey", 21),
          ("Karan", 22)]

data = lambda age: age[1] >= 18

filtered_data = list(filter(data, people))

for i in filtered_data:
    print(i)
