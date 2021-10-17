dict_a = dict()
print(dict_a)


dict_b = {
    "Name": "Narasimha",
    "Lastname": "Reddy",
    "Age": 25
}
print(dict_b['Name']) # Accessing  -- raises Keyerror, if key not found

print(dict_b.get('Nae')) # Returns none if not found

print('Name' in dict_b) # Membership check


# Adding , modifying, deleting key-value pair

dict_b['City'] = "Hyderabed"

dict_b['Age'] = 24

del dict_b['Lastname']

print(dict_b)

print(dict_b.keys())
print(dict_b.values())
print(dict_b.items())

for key in dict_b.keys():
    print(key)


print(list(dict_b.keys()))


for key, value in dict_b.items():
    print(key, value)
    print("{} {}".format(key, value))



list_a = [('Name', "Nara"), ("Age", 25)]
print(dict(list_a))

# keys must be immutable ---- Can use Integers, Floats, Strings, Tuples (only all items are immutable)
# We cannot use Lists, Sets, Dictionaries -- as Keys


dict_c = {'Name': 'Teja', "Age": 24}

dict_d = dict_c

dict_d['Age'] = 25

print(dict_c)
print(dict_d) # Both are same and both are modified


# So to avoid this case
dict_e = dict_c.copy()
dict_e['Age'] = 26

print(dict_c) # Not mofidied
print(dict_e) 


# Opearations on Dictionaries
print(len(dict_e))

# membership check
if "Name" in dict_e:
    print(True)

dict_e.clear()
print(dict_e)


# Iterating -- We can't add/remove dictionary keys while iterating
print(dict_b)
for k in dict_b.keys():
    print(k)




# Arbitrary function arguments --- *args --- Can define a function to receive any number of arguments

# Variable length arguments

def more_args(*args):
    print(args)


more_args()
more_args(1,2,3)


# If we are passing the argument as List -- we need to unpack that

def un_pack_args(arg1, arg2):
    print(arg1 + " " + arg2)


data = ["Hello", "Ram"]
data1 = {"arg1": "Hello", "arg2":"Ram"} # must be same keyword as in function declaration

un_pack_args(*data)
un_pack_args(**data1) 


# When we are passing multiple keyword arguments -- use **kwargs

def more_kwargs(**kwargs):
    print(kwargs)

    for i,j in kwargs.items():
        print('{}: {}'.format(i, j))

more_kwargs(a=1, b=2)
more_kwargs()


# kwargs is a dictionary -- we can iterate over it


def stu_info(*args, **kwargs):
    print(args)
    print(kwargs) 

stu_info("Math", "Science", nama="Ramu", Age = 22)




# Print consecutive sum list [1,2,3,4] --- [3,5,7] --- [8, 12] -- [20] -- fisrt and second numbers sum

def get_con_sum(num_list):
    row_con_sum = []
    for i in range(len(num_list) - 1):
        row_con_sum.append(num_list[i] + num_list[i+1])
    
    return row_con_sum

def get_con_sum_list(num_list):
    while len(num_list) > 1:
        con_sum = get_con_sum(num_list)
        print(con_sum)
        num_list = con_sum

num_list = [1, 2, 3, 4]

print(num_list)
get_con_sum_list(num_list)




# Print group of colors -- as {r:5, g:3, b:3}

colors = ['r:1','g:3','b:2', 'b:1', 'r:4']

colors_dict = {}

for item in colors:
    each_item = item.split(':')
    color_name, color_value = each_item[0], int(each_item[1])

    if color_name in colors_dict:
        colors_dict[color_name] = colors_dict[color_name] + color_value
    else:
        colors_dict[color_name] = color_value

print(colors_dict)



# Add square of nums to dictionary

number = 3

dict_f = dict() #  or {}

for i in range(1, number+1):
    dict_f[i] = i*i

print(dict_f)



# .items() -- will give with dict_item([ -- ]) --- if we do sort or list()-- it will converted to normal list

# We can't directly modify the keys in dictionary while iterating 

# Make a copy and modify in that copy 

# Rename a Key --- apples with pomegranates

fruits = {"apples": 10, "bananas": 4, "oranges": 7}

a_new = "pomegranates"

fruits_items = list(fruits.items())
fruits_items_copy = fruits_items.copy()

print(fruits_items)

for i in range(len(fruits_items)):
    if fruits_items[i][0] == "apples":
        update_item = (a_new, fruits_items[i][1])
        fruits_items_copy[i] = update_item

print(fruits)
print(fruits_items_copy)


# Combine 2 dictionaries using dict1.update(dict2) ****

