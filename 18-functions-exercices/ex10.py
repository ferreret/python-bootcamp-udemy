'''
multiply_even_numbers([2,3,4,5,6]) # 48
'''


def multiply_even_numbers(list_numbers):
    even_numbers = [number for number in list_numbers if number % 2 == 0]
    if even_numbers.count == 0:
        return 0
    result = 1
    for number in even_numbers:
        result *= number
    return result


print(multiply_even_numbers([2, 3, 4, 5, 6]))
