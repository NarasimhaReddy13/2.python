matrix_a = [[1,2,5],[8,9,10],[10,20,15]]

# m,n ---- conv str to int list --- 

print(max(max(matrix_a))) # Prinits maximum number
print(min(min(matrix_a)))

sum_matrix_a = 0
for item in matrix_a:
    sum_matrix_a += sum(item)

print("Sum of elements", sum_matrix_a)



# print max number row and max number column

max_row = max(matrix_a)
print("Max Number Row", max_row)

max_num_index = max_row.index(max(max_row))

max_col_list = []
for item in matrix_a:
    max_col_num = item[max_num_index]
    max_col_list.append(max_col_num)


print("Max Number Column", max_col_list)



print("*********** Transpose ***********")

transp_matrix = []
m = 3
n = 3
for i in range(n):
    row = []
    for j in range(m):
        row.append(matrix_a[j][i])

    transp_matrix.append(row)

print(transp_matrix)


# row -- max , min, sum
# For column min, max, sum ---- First do transpose , and do same as of row


# Principal Diagonal Elements
diagonal_elements_list = []
for i in range(m):
    if i < n:
        diagonal_elements_list.append(matrix_a[i][i])

print(diagonal_elements_list)

# 2

diagonal_elements_list2 = []
for i in range(m):
    for j in range(n):
        if i == j:
            diagonal_elements_list2.append(matrix_a[i][j])

print(diagonal_elements_list2)



print(matrix_a)
# Lower Triangle Matrix 
for i in range(m):
    row_element = []
    for j in range(n):
        if j <= i:
            row_element.append(matrix_a[i][j])

    print(row_element)





# Replace a Value in matrix
rep_val = 12
original_val = 10
# Replace 10 with 12 in all occurances
updated_matrix = []
for item in matrix_a:
    for i in range(len(item)):
        if item[i] == original_val:
            item[i] = rep_val
    updated_matrix.append(item)

print(updated_matrix)




# Add 2 matrices
added_matrix = []
for i in range(m):
    rows = []
    for j in range(n):
        value = matrix_a[i][j] + matrix_a[i][j]
        rows.append(value)
    
    added_matrix.append(rows)

print(added_matrix)
