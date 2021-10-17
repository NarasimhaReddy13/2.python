import math

print(math.factorial(5))
print(math.pi)


import math as m1  # alias

print(m1.sqrt(25))

from math import factorial # import specific module
print(factorial(5))

# we can also alias this specific module




# random , radint()
import random
random_int = random.randint(1, 10)
print(random_int)

random_char = random.choice(["A","C","N"])
print(random_char)


# map()
numbers = [1,2,3,4]

def square(n):
    return n*n

print(list(map(square, numbers)))
print(list(map(int, numbers)))


# filter()
num_filters = [1,0,-1,5,-4]

def is_positive(num):
    return num > 0

filter_list = list(filter(is_positive, num_filters))
print(filter_list)



from functools import reduce

def sum_nums(a,b):
    return a+b

num_reduce = [1,2,3,4]
sum_of_nums = reduce(sum_nums, num_reduce)
print(sum_of_nums)

print(sum(num_reduce))


# Namespace ----- can use same name referring different things in different Namespaces

def greet_1():
    a = "Hello"
    print(a, id(a))

def greet_2():
    a = "Hey"
    print(a, id(a))


greet_1()
greet_2()



# Namespaces 
import math
a = 2  # Global

def foo():
    b = 6  # Local
    print(a+b) # Builtin

foo()




# Global and Local Variable-- Namespaces
def fun():
    print(x)

x = "Global"

fun()


# Local
def local():
    y = "Local"
    print(y)

local()
# print(y) --- raises error y is not defined



# Local Import
def local_import():
    import math
    print(math.pi)

local_import()
# Outside this function math is not available




# We can modify the Global Variables --- 
    # global keyword is used to define a name to refer to the value in Global Namespace.

z = "Global Variable"

def global_space():
    global z
    z = "Global Change"

print(z)
global_space()
print(z)


# Examples for Exceptions

def divide(a,b):
    print(a/b)

#divide(5, 0) # ZeroDivisionError

#divide("5", "10") -- Input must be within expected values -- TypeError or KeyError



try:
    m = int(5)
    n = int(0)
    o = m/n
    print(o)

except ZeroDivisionError:
    print("Denominator can't be 0")
except ValueError:
    print("Input should be an integer")
except:
    print("Unhandled Exception")