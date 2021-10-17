tuple_a = (1,) # with single item
print(type(tuple_a))
print(tuple_a)

tuple_b = (1)
print(type(tuple_b))  # returns int

# Can access 

print(tuple_a[0])

# Doesn't support modification
# tuple_a[0] = "Nani"

# print(tuple_a) --- error

tuple_c = (1, "Hai", 3.2, False)

print(len(tuple_c))
# Can iterate
# Can perform slicing and extended slicing


string = "Nara"
print(tuple(string)) # converting to tuple


list_tuple = ['n', 3]
print(tuple(list_tuple))

print(5 in list_tuple) # membership check  -- in, not in


print('ar' in string) # String membership check



a = 2
tuple_d = (1,2,a)
print(tuple_d)

c = ()
print(c)

print(tuple_c * 2)

tuple_e = ("Orange", [5,4,2], (5,8,6))
print(tuple_e[1][1])





# Sets
set_a = {1,"Nara", True, 5.2, 1}
print(type(set_a))
print(set_a)   # ---- need not to be same order as we defined -- duplicated are eliminated automatically 


# As sets are immutable , lists are mutable --- sets must not containt lists

# set_b = {"a", [1, 2]} # wrong --- will give error

set_c = set()

# Converting to set -- takes any sequence as argument and converts to set by avoiding duplicates

set_d = set([1,1,2,4,4])  # List to Set -- can be any string "apple" or tuple (1, 2 , 1)
print(set_d)



# As Sets are Unordered -- we can't access or change items of a set using -- Indexing, Slicing

# Can perform some actions

set_e = {1,2,4,6,"Hello", 5.2}

set_e.add(4)

set_e.update([5,7])

set_e.discard(1)

# set_e.remove(10) # Removes if present -- else raise error

print(set_e)



# Union  --- All elements without duplicates
set_f = {4,2,8}
list_g = [2,0]   # may be set or list
set_h = {2, 0}


print(set_f | set_h)
print(set_f.union(list_g))


# Intersection ----- common elements
print(set_f & set_h)
print(set_f.intersection(list_g))


# union or intersection ---- converts to a set 

# Difference -- elements which are only in first set

print(set_f - set_h)
print(set_f.difference(list_g))


# Symmetric Difference --- Uncommon elements 

print(set_f ^ set_h)
print(set_f.symmetric_difference(list_g))  # As 2 is common --- it is discarded




# Set Comparisons:
# issubset() --- If all elements of set_2 are in set_1

set_i = {1, "a", 3.2, 6}
set_j = {"a", 3.2}

print(set_j.issubset(set_i))  # returns True or False

# superset() --- True , if all elements of 1st set are in 2nd set -- viceversa

print(set_i.issuperset(set_j))

print(set_i.isdisjoint(set_j))  # True, if no coomon elements




print("************** Problems -------- **********")

# Replace last element in each tuple with the given number
tuple_num = 50
list_tuple = [(2,10,0), (5,20,30), (2,10), (5,), (2,50)]

new_replaced_list = []
for item in list_tuple:
    updated_tuple = item[:-1] + (tuple_num,)
    #updated_tuple = item[:len(item)-1] + (tuple_num,)

    new_replaced_list.append(updated_tuple)

print(new_replaced_list)










# Get multiples of 2 , multiples of 3 --- with number of multiples based on input
# print only multiples of 2 -- not the multiples of 3

# print all uncommon multiples

num_of_multiples = int(5)

mul_2 = set()
mul_3 = set()

for i in range(1,num_of_multiples +1):
    mul_2.add(2*i)
    mul_3.add(3*i)

print(sorted(list(mul_2 - mul_3)))
print(sorted(list(mul_2.symmetric_difference(mul_3))))



# To get pair sum --- we can iterate on remaining list or directly using for nested loop



# Program to find common elements in N Sets

# 3 --sets
list_x = 2,4,6,8,10
list_y = 4,8,10,12,16,10
list_z = 2,5,10,12,15,204

# [4, 10, 12] -- result

# num_sets = int(3)
# nums_list = []

# def get_intersection(nums_list):
#     result1 = nums_list[0]

#     for num_set in nums_list:
#         result1 = result1.intersection(num_set)
    
#     return result1

# for i in range(num_sets):
#     values_list = list(map(int, input().split()))
#     values_set = set(values_list)

#     nums_list.append(values_set)

# result_set = get_intersection(nums_list)



print("********* Rotate D Times *************")

# lOGIC : -- If rotate_times > length -- we are repeating the same rotation again

rotate_list = [1,2,3,4,5,6]
rotate_times = int(10)

rotate_times_count = rotate_times % len(rotate_list)
first_part = rotate_list[:rotate_times_count]

last_part = rotate_list[rotate_times_count:]

last_part.extend(first_part)

print(last_part)





nested_str = ["Narasimha"]
print(nested_str[0][1])


print("String Formatting using { placeholders } or Numbering or Naming Placeholders ----- ")


place_name = "Narasimha"
place_age = 25

# No type conversion is required
print("Hello {}. Your age is {}.".format(place_name, place_age))

print("Hello {0}. Your age is {1}.".format(place_name, place_age))

print("Hello {name}. Your age is {age}.".format(name = place_name, age = place_age))



# list(map(int, input().split()))
# max(result)


# Get Nested Item index

nes_list = [(2, 4, 6, 8), (5, 15, 30, 35), (7, 14, 21)]

n = int(4)
for item in nes_list:

    if n in item:
        index = nes_list.index(item)
        n_index = item.index(n)
        print(str(index) + " " + str(n_index))
        break



print("Character Frequnecy")

chr_freq = "Pop Up"
lower_case = chr_freq.lower()

set_lower_case = set(lower_case)
set_lower_case.discard(" ")


for item in sorted(set_lower_case):
    print("{}: {}".format(item, lower_case.count(item)))