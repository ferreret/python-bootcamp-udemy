'''
remove_every_other([1,2,3,4,5]) # [1,3,5] 
remove_every_other([5,1,2,4,1]) # [5,2,1]
remove_every_other([1]) # [1] 
'''


def remove_every_other(input_list):
    return [x for ind, x in enumerate(input_list) if ind % 2 == 0]


print(remove_every_other([1, 2, 3, 4, 5]))  # [1,3,5]
print(remove_every_other([5, 1, 2, 4, 1]))  # [5,2,1]
print(remove_every_other([1]))  # [1]
