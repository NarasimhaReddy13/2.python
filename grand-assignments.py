# Prefix , Suffix

a = "ramisgood"
b = 'goodforall'

length = len(b)

if len(a) > len(b):
    length = len(a)

for i in range(1, length +1):
    if b[:i] == a[-i:]:
        print(a[-i:])
        break

else:
    print("No Overlapping")



# Anti-Diagonal Elements ---
"""
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

solution: 
1
2 5
3 6 9
4 7 10 13
8 11 14
12 15
16
"""

m,n = int(4), int(4)
matrix_a = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]

rows = m+n-1

for i in range(rows):
    row = ''
    for j in range(i+1):
        if j < m and i-j < n:
            row += str(matrix_a[j][i-j]) + " "
    
    print(row)


# Matrix Rotation
# Polynomials


# Word Count -- in sorted order
word1 = ['Hello', 'world', 'welcome', 'to', 'my', 'world']

set_word = set(word1)

indexes = []
for item in set_word:
    indexes.append(word1.index(item))

for item in sorted(indexes):
    print(word1[item] + ": " + str(word1.count(word1[item])))