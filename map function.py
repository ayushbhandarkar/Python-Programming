# Example 1
# ls = [4, 2, 5, 8, 6, 9, 27]
# ans = list(map(lambda x: x*2, ls))
# print(ans)


# Example 2
Nike = [("shirts", 20.00),
        ("jeans", 30.00),
        ("t-shirts", 18.00),
        ("jacket", 35.00)]

to_rupee = lambda data: (data[0], data[1]*82)   # This function will update data[1]

Nike_Store = list(map(to_rupee, Nike))

for i in Nike_Store:
    print(i)


