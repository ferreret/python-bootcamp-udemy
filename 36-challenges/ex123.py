'''
EXAMPLES:


list1 = [
  [ 1, 2 ],
  [ 3, 4 ]
]
 
sum_up_diagonals(list1) # 10

list2 = [
  [ 1, 2, 3 ],
  [ 4, 5, 6 ],
  [ 7, 8, 9 ]
]
 
sum_up_diagonals(list2) # 30
 
list3 = [
  [ 4, 1, 0 ],
  [ -1, -1, 0],
  [ 0, 0, 9]
]

sum_up_diagonals(list3) # 11

list4 = [
  [ 1, 2, 3, 4 ],
  [ 5, 6, 7, 8 ],
  [ 9, 10, 11, 12 ],
  [ 13, 14, 15, 16 ]
]
 
sum_up_diagonals(list4) # 68
'''


def sum_up_diagonals(arr):
    total = 0

    for i, val in enumerate(arr):
        total += arr[i][i]
        total += arr[i][-1-i]
    return total


# def sum_up_diagonals(matrix):

#     sum_diag = 0

#     sum_diag = sum_diag_matrix(matrix)
#     reversed_matrix = [list(reversed(x)) for x in matrix]
#     sum_diag += sum_diag_matrix(reversed_matrix)

#     # print(reversed_matrix)

#     return sum_diag


# def sum_diag_matrix(matrix):
#     x = len(matrix)
#     y = len(matrix[0])
#     result = 0
#     for count_x in range(0, x):
#         for count_y in range(0, y):
#             if count_x == count_y:
#                 result += matrix[count_x][count_y]
#     return result


list1 = [
    [1, 2],
    [3, 4]
]

print(sum_up_diagonals(list1))  # 10

list2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(sum_up_diagonals(list2))  # 30

list3 = [
    [4, 1, 0],
    [-1, -1, 0],
    [0, 0, 9]
]

print(sum_up_diagonals(list3))  # 11

list4 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print(sum_up_diagonals(list4))  # 68
