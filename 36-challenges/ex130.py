'''
three_odd_numbers([1,2,3,4,5]) # True
three_odd_numbers([0,-2,4,1,9,12,4,1,0]) # True
three_odd_numbers([5,2,1]) # False
three_odd_numbers([1,2,3,3,2]) # False
'''


def three_odd_numbers(numbers):
    len_numbers = len(numbers)
    for cursor in range(2, len_numbers):
        sum_test = numbers[cursor - 2] + numbers[cursor - 1] + numbers[cursor]
        if sum_test % 2 == 1:
            return True
    return False


print(three_odd_numbers([1, 2, 3, 4, 5]))  # True
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))  # True
print(three_odd_numbers([5, 2, 1]))  # False
print(three_odd_numbers([1, 2, 3, 3, 2]))  # False
