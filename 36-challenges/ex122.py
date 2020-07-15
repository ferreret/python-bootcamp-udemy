'''
find_the_duplicate([1,2,1,4,3,12]) # 1
find_the_duplicate([6,1,9,5,3,4,9]) # 9
find_the_duplicate([2,1,3,4]) # None
'''


def find_the_duplicate(numbers):
    duplicates = [num for num in numbers if numbers.count(num) > 1]
    return duplicates[0] if len(duplicates) > 0 else None


print(find_the_duplicate([1, 2, 1, 4, 3, 12]))  # 1
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))  # 9
print(find_the_duplicate([2, 1, 3, 4]))  # None
