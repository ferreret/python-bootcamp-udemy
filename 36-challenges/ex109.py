'''
list_check([[],[1],[2,3], (1,2)]) # False
list_check([1, True, [],[1],[2,3]]) # False
list_check([[],[1],[2,3]]) # True
'''


def list_check(input_list):
    return all(isinstance(list_item, list) for list_item in input_list)


print(list_check([[], [1], [2, 3], (1, 2)]))  # False
print(list_check([1, True, [], [1], [2, 3]]))  # False
print(list_check([[], [1], [2, 3]]))  # True
