# Greatest Common Divisor -- max number which divides the given numbers

a = 2
b = 4

if a>b:
    max_num = a
else:
    max_num = b

gcd = max_num

for i in range(1, gcd +1):
    if (a%i == 0 and b%i == 0):
        gcd = i

print("GCD", gcd)



#LCM --- 1st or Least common multiple -- which exactly divides the number 

lcm = max_num

# lcm = false

for i in range(max_num, (a*b + 1)):
    # if not lcm:
    if (i%a == 0 and i%b == 0):
        lcm = i
        # lcm = True


print("LCM", lcm)



# --- Hallow Inverted Full Pyramid --
# 1 2 3 4 5
#  1     4
#   1   3
#    1 2
#     1


number = int(10)

for i in range(1,number+1):
    row = number - (i - 1)

    left_spaces = ' '*(i-1)
    if row > 2 and row < number:
        inner_spaces = "  " * (row-2)
        
        print(left_spaces + "1 " + inner_spaces + str(row))

    else:
        final_str = ''
        for j in range(1,row+1):
            final_str += str(j) + " "

        print(left_spaces + final_str)




print("*********** Perfect Squares in the given range of Numbers **********")

strt_num = 9
end_num = 100

for i in range(strt_num, end_num+1):
    if i**(0.5) == int(i**(0.5)):
        print(i)