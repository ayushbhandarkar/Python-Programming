# wap to merge two lists
list1 = [12, 20, 30, 41, 50, 80]
list2 = [10, 25, 35, 50, 41, 70]
print(" List 1 : ", list1)
print(" List 2 : ", list2)

list3 = list1 + list2
list3.sort()
print(" New list in ascending order : ", list3)

big = list3[-1]
print(" Biggest number : ", big)

s_big = list3[-2]
print(" Second Biggest : ", s_big)

small = list3[0]
print(" Smallest number : ", small)

s_small = list3[1]
print(" Second Smallest number : ", s_small)

new_list = [big, s_big, small, s_small]
print(" New list of Smallest, 2nd Smallest, Biggest, 2nd Biggest: ", new_list)
sum = 0
for i in new_list:
    sum += i

print(" Sum of new list : ", sum)



# sayyedfaraz128@gmail.com