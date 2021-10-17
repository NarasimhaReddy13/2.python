print("Prime Numbers Range")
print("-------- Verify for Python Extension ----------")

a = 10
b = 20
for i in range(a,b+1):
    fact = 0
    for j in range(2,i):
        if (i%j) == 0:
            fact += 1
                           
    if fact == 0:
        print(i)


print("------------------")
print("Triangle Numbers Range")

c = 5
d = 1 
for i in range(1,c+1):
   row = ''
   for j in range(1,i+1):
      row += str(d) + " "
      d = d + 1
   print(row)




print('----------------------------')
print('Kth Largest Factor')

num = 12
fac_num = 2

factor = num

factor_count = 0
factor_condition = False

for i in range(1,num+1):
    if not factor_condition and (num%factor == 0):
        factor_count += 1
        if factor_count == fac_num:
            print(factor)
            factor_condition = True
    factor = factor - 1


# If fac_num is > factors_count ---- Use list to print factor as 1


print("-------------- pass, continue ----------------")

for i in range(5):
    if i == 3:
        pass
    print(i)
print("pass")

for i in range(5):
    if i == 3:
        continue
    print(i)
print("continue")


print("---------- First Prime Number in the given range --------")

e = -2
f = 1

if e < 2:
    e = 2

no_primes_count = 0

for i in range(e, f+1):
    is_prime = True
    for j in range(2, i):
        if (i%j == 0):
            is_prime = False
            break
    if is_prime:
        print(i)
        no_primes_count += 1
        break

if no_primes_count == 0:
    print("No Primes in range")



print("---- Sum of Non-Prime Numbers ------------")

# g = int(input())
# non_prime_sum = 0

# for i in range(g):
#     h = int(input())

#     if (h > 3 and (h%2 == 0 or h%3 == 0 or h%5 == 0 or h%7 == 0)):
#         non_prime_sum = non_prime_sum + h

# print(non_prime_sum)


print('-------------- Hollow Diamond ----------------- ')

#     *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *

k = int(10)
print(' ' * (k-1) + "*")

inner_spaces_count = -1
for i in range(2,k+1):
    inner_spaces_count += 2
    inner_space = " " * inner_spaces_count

    print(" " * (k-i) + "*" + inner_space + "*")

for i in range(1,k-1):
    inner_spaces_count -= 2
    inner_space = " "*inner_spaces_count
    print(" " * (i) + '*' + inner_space + "*")

print(' ' * (k-1) + "*")


print("Hello\"Narasimha")

print("------------ Is Subsequent or Not -----------------")

first_word = "Narasimha"
sub_seq = "simha"

index = 0
for item in first_word:
    if sub_seq[index] == item:
        index += 1
        if index == len(sub_seq):
            break

if index == len(sub_seq):
    print("Sub-sequent")
else:
    print("Not a sub-sequent")



print("--------------- Number Pyramid ---------------")

#     1
#    212
#   32123
#  4321234
# 543212345

m = 5
for i in range(1,m+1):
    left_nums = ''
    right_nums = ''
    for j in range(1,i+1):
        right_nums = str(j) + right_nums
        left_nums = left_nums + str(j)
    print(' ' * (m-i) + right_nums + left_nums[1:])



    



n = int(5)
for i in range(1,n+1):
    print(' ' * (n-i) + "/" + " " * (2*i - 2) + "\\")
    
for i in range(1,n+1):
    print(' ' * (i-1) + "\\" + " " * (2*n-2*i) + "/")




print("*********** Day Name - Given Day of Month and days ***********")

day = "Monday"
n_day = int(16)
days = ["Sunday", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

index = days.index(day)
rem_list = days[index:]
len_rem_list = len(rem_list) + 1
    
rem_days = n_day%7

if rem_days >= len_rem_list:
    print(days[rem_days - len_rem_list])
else:
    print(days[rem_days + index - 1])