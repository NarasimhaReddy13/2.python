import datetime

date_obj1 = datetime.date(2021, 8, 20) # must be valid year, month, date only
print(date_obj1)


#

from datetime import date
date_obj2 = date(2021, 8, 20)
print(date_obj2)

#

# ---- date_obj3 = date(2021, 2, 31) # ValueError: day is out of range for month

#
today_date = datetime.date.today()
print(today_date)

# year, month, date
print(today_date.year)
print(today_date.month)
print(today_date.day)


# Working with time

from datetime import time

time_obj = time(11, 34, 56)  # (hours, minutes, seconds) --- must be valid time oly

print(time_obj)
print(time_obj.hour)
print(time_obj.minute)
print(time_obj.second)


print(time_obj.microsecond)

#----- datetime

from datetime import datetime

date_time_obj = datetime(2018, 8, 28, 10, 15, 16) # (yr, m, day, hr, min, secs)
print(date_time_obj)  # can access - hour, minute, day ---- 

dto_current = datetime.now()
print(dto_current)


# --- We can also give date for datetime obj -- all other are taken as zero

dtobj = datetime(2019, 2, 28)
print(dtobj)


# formatting datetime ---- strftime(format) while printing 
# From object to string


now = datetime.now()
for_date1 = now.strftime("%d-%b-%Y %H hours %M minutes %S seconds %p %A")

print(for_date1)


# ------- strptime() -- while creating
# from string to object

string_datetime = "20 August 2021"

str_to_obj = datetime.strptime(string_datetime, "%d %B %Y")
print(str_to_obj)



####################################

from datetime import timedelta, datetime

curr_datetime = datetime.now()

delta = timedelta(days=365, hours=12)

new_datetime = curr_datetime + delta

print(new_datetime)


#################################

dt1 = datetime.now()
dt2 = datetime(2018, 6, 14)

duration = dt1 - dt2
print(duration)
print(type(duration))


#################

a = datetime.strptime("Feb 20 2021", "%b %d %Y")
b = datetime.strptime("Feb 23 2021", "%b %d %Y")

num_of_days = (b - a).days


for i in range(num_of_days + 1):
    delta1 = a + timedelta(days = i)
    print(delta1)


#################

c = datetime.strptime("2 Jul 2000", "%d %b %Y")

day = c.strftime("%A")

print(day)


###################### count monday's 

strt_date, end_date = 2015, 2017

monday_days = 0

for year in range(int(strt_date), int(end_date) + 1):
    for month in range(1, 13):
        day = datetime(year, month, 1)
        name_day = datetime.strftime(day, "%A")

        if name_day == "Monday":
            monday_days = monday_days + 1 
            
print(monday_days)


######## UNIX timestamp

seconds = timedelta(seconds = 1284105682)
uniq_time = datetime(1970, 1, 1)

result_time = uniq_time + seconds
print(result_time.strftime("%Y-%m-%d %H:%M:%S"))






############### Max-Contiguous Subarray #############
list_array = [-2,-3,4,-1,-2,1,5,3]

sum_dict = {}

for i in range(len(list_array)):
    for j in range(i+1, len(list_array)):
        sum_dict[tuple(list_array[i:j])] = sum(list_array[i:j])

keys = list(sum_dict.keys())
values = list(sum_dict.values())

max_value_index = values.index(max(values))
print(*keys[max_value_index])



# ############ 3 word combination in lexicographical order ######

inp = ["apple", "is", "a", "fruit"]
words = sorted(inp)
str_inp = list(range(len(words)))

combi_1 = []
for word in str_inp:
    combi_1.append([word])

    
combi_2 = []
for i in combi_1:
    for j in str_inp:
        if j > i[-1]:
            combi_2.append(i + [j])
            
combi_3 = []
for i in combi_2:
    for j in str_inp:
        if j > i[-1]:
            combi_3.append(i + [j])
            
word_combi = []
for com in combi_3:
    word_com = []
    for index in com:
        word_com.append(words[index])
    word_combi.append(tuple(word_com))
            
set_word = sorted(set(word_combi))

# print(combi_1)
# print(combi_2)

for item in set_word:
    print(*item)
    