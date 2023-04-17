# Exceptional handling
def reference(*data):

    try:
        # sum=0
        for ele in data:
            sum += ele
        print(" Sum of elements : ", sum)
    except TypeError:
        print(" We can't add list or any collection with integer ")
    except:
        print(" invalid value passed Try Again")
    finally:
        print(" Happy coding")


reference([1, 2, 3, 4, 5])      # if we pass list as an reference we can't add that list in integer number
