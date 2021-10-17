a = 5
list_a = [5, "Nara", a, True, 8.2]

print(list_a)

print([1, list_a]) # Nested List

print(len(list_a))

print(list_a[1])

for item in list_a:
    print(item)


print(list_a + [1, "Hello"])  # Concatination

# Adding Items to list

list_b = []
for i in range(1,4):
    list_b += [i]

print(list_b)

print(list_b * 3) # Repetition

# List Slicing --- to obtain a part of a list

print(list_a[1:3])
print(list_a[:3]) # If start Index is not mentioned -- takes from start ( similary for end index)


# Extended Slicing

print(list_a[1:len(list_a):2])

print(list("RED")) # Cconverting to list
print(list(range(4))) #------ Important


# Lists are Mutable -- Items at any position can be updated
print(list_a)
list_a[0] = 1
print(list_a)


# Strings are Immutable
message = "Narasimha"
# message[2] = "a"
print(message)  # TypeError -- str Object doesn't support item assignment



print("Narasimha".split("a"))
print("a".join(['N', 'r', 'simh', '']))


neq_step_list = [5,4,3,2,1]

print(neq_step_list[4:2:-1])

print("program"[6:0:-2])


rev_str = "The cat is on the mat."

rev_str_split = rev_str.split()

splitted_word = []

for each in rev_str_split:
    splitted_word += [each[::-1]]


rev_word = " ".join(splitted_word)
print(rev_word)




print("-----------------------------")

list_m = "1,2,3".split(",")
list_n = "4,5,6".split(",")

len_of_list_m = len(list_m)
x = len_of_list_m - 1

for i in range(len_of_list_m):
    num_1 = list_m[i]
    num_2 = list_n[x-i]
    result = str(num_1) + " " + str(num_2)
    print(result)



print("----------- -------------- - -  -- - --  ---- ")

# Functions ---- using in lists

def add_item_list(list_x):
    # list_x += [3] -- [1,2,3] --- as they both are referring same object
    list_x = list_x + [3]  # -- [1, 2] -- default args are evaluated only once when the function is defined
    return list_x

list_o = [1,2]
add_item_list(list_o)
print(list_o) 


def add_item(list_y = []):
    list_y += [3]
    print(list_y)

add_item()
add_item([1,2])
add_item()