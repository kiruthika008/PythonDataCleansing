mylist=[1,2,3,4,5]


# sum of list using recursive functions
def func(mylist):
    if len(mylist)==1:
        return mylist[0]
    else:
        return mylist[0]+func(mylist[1:])

print(func(mylist))


#reverse the string
def reverse_func(mystr):
    if len(mystr)==1:
        return mystr
    else:
        return mystr[-1]+reverse_func(mystr[:-1])
print(reverse_func("kiruthika"))

def simple_rev(mystr):
    return mystr[::-1]
print(simple_rev("kiruthika"))

def factorial(num):
    if num==1:
        return 1
    else:
        return num*factorial(num-1)
print(factorial(5))