def greet(myName):
    message = "Hello " + myName
    print(message)

name = "Narasimha"
greet(myName = name)   # or simply --- name


# We can't print directly outside the function -- Use below code

def greet1(myName):
    message = "Hello " + myName
    return message

name1 = "Reddy"
greeting = greet1(myName = name1)
print(greeting)


# Keyword args -- order doesn't matter ( assigning keyword matters )
def greet_nara(arg_1, arg_2):
    print(arg_1 + ' ' + arg_2)

arg1 = "Hello"
arg2 = "Ram"

greet_nara(arg_2= arg1, arg_1=arg2)
greet_nara(arg_2= arg2, arg_1=arg1)
# greet_nara(arg_1=arg2) ----- gives error

# Positional Arguments --- passed without args names , order matters

greet_nara(arg1, arg2)
greet_nara(arg2, arg1) # If num of args are not matched gives error


# without passing args in call --- can use default values

def greet_narasimha(arg_1 = "Hi", arg_2="Nani"):
    print(arg_1 + ' ' + arg_2)

args1 = "Hello"
args2 = "Ram"
greet_narasimha()
greet_narasimha(args1) # If we want to pass it for 2nd ard use keyword argument 



# Non-default arguments cannot follow default arguments

#  def error_greet(arg1="Hai", arg2) -- uncomment and verify

# Passing immutable objects --- 

def increment(a):
    a += 1
    return a

a = int(5)
b = increment(a)
print(a)
print(b)

# Even though variable names are same -- they are referring 2 different objects 



print("Kth Largest Number")

list_a = [2,3,-1,0,5,4,10]
k_num = 2

int_list_a = []
for item in list_a:
    int_list_a += [int(item)]

rev_sorted_list = sorted(int_list_a, reverse=True)
print(rev_sorted_list[k_num - 1])

sorted_list = sorted(int_list_a)
print(sorted_list[-k_num])



print("****************** Recurssion ************* ")

# Factoral of a Number using recurssion

number_1 = 5

def factorial_num(num):
    if num <= 1:
        return 1  # If we miss this -- returns error as max recurssion depth exceeded
    return num * factorial_num(num -1)

print(factorial_num(number_1))


print('****** Sum of Digits in a Number ********')

number = int(54321)

def sum_of_digits(number):
    if number < 10:
        return number
    return number%10 + sum_of_digits(number // 10)


print(sum_of_digits(number))



print('**** sort() --  sorted() *****')

list_to_sort = [1,5,4,0,-1]
print(list_to_sort.sort())
print(list_to_sort)  # -- modifies the original list



list_to_sorted = [1,5,4,0,-1]
print(sorted(list_to_sorted))
print(list_to_sorted) # -- doesn't modifies the original list



print("---- List Methods ------")

list_methods = [1,"Hello"]
list_methods.append("Nani")

pop_count = 2

for i in range(pop_count):
    list_methods.pop()  # To remove the last items

print(list_methods)



# Remove all the Occurances ****
remove_list_occuranes = [5, 10, 20, 35, 5, 50, 20, 100, 200, 10, 5, 150, 100, 100]
remove_num = int(5)

for item in range(remove_list_occuranes.count(remove_num)):
    remove_list_occuranes.remove(remove_num)

print(remove_list_occuranes)




# Nth Term in fibonacci series **** add items as list

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_list(n):
    fibo_list = []
    for i in range(n):
        fibo_num = fibonacci(i)
        fibo_list.append(fibo_num)
    return fibo_list

fibo_num = 8
print("fibonacci of 21 -- fibo(n-1) + fibo(n-2)", fibonacci_list(fibo_num))
