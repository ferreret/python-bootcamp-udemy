'''
mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]) # 4
'''

# define mode below:


def mode(numbers):
    numbers_dict = {num: numbers.count(num) for num in numbers}
    max_key = max(numbers_dict, key=numbers_dict.get)
    return max_key


print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))
