'''
def isEven(num):
    return num % 2 == 0

partition([1,2,3,4], isEven) # [[2,4],[1,3]]
'''


def isEven(num):
    return num % 2 == 0


def partition(input_list, func):
    truthy_list = [item for item in input_list if func(item)]
    falsy_list = [item for item in input_list if not func(item)]
    return [truthy_list, falsy_list]


print(partition([1, 2, 3, 4], isEven))  # [[2,4],[1,3]])
