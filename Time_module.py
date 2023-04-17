from time import time, ctime, localtime

epoch = time()
# print(epoch)

et = ctime(epoch) # et stands for epoch time
# print(et)

stobj = localtime()
# print(stobj)

print("Date : ", stobj.tm_mday, end="/")
print(stobj.tm_mon, end="/")
print(stobj.tm_year)

print("Time : ", stobj.tm_hour, end=":")
print(stobj.tm_min, end=":")
print(stobj.tm_sec)

