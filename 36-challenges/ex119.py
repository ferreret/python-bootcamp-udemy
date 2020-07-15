'''
range_in_list([1,2,3,4],0,2) #  6
range_in_list([1,2,3,4],0,3) # 10
range_in_list([1,2,3,4],1) #  9
range_in_list([1,2,3,4]) # 10
range_in_list([1,2,3,4],0,100) # 10
range_in_list([],0,1) # 0
'''


def range_in_list(num_list, start_index=0, end_index=None):
    if not end_index or end_index > len(num_list):
        end_index = len(num_list)
    else:
        end_index += 1

    return sum(num_list[x] for x in range(start_index, end_index))


# def range_in_list(lst, start=0, end=None):
#     end = end or lst[-1]
#     return sum(lst[start:end+1])


print(range_in_list([1, 2, 3, 4], 0, 2))  # 6
print(range_in_list([1, 2, 3, 4], 0, 3))  # 10
print(range_in_list([1, 2, 3, 4], 1))  # 9
print(range_in_list([1, 2, 3, 4]))  # 10
print(range_in_list([1, 2, 3, 4], 0, 100))  # 10
print(range_in_list([], 0, 1))  # 0
