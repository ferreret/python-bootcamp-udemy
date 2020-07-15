'''
is_odd_string('a') # True
is_odd_string('aaaa') # False
is_odd_string('amazing') # True
is_odd_string('veryfun') # True
is_odd_string('veryfunny') # False
'''


def is_odd_string(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0
    return total % 2 == 1


# def is_odd_string(input_string):
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     return sum(alphabet.find(letter) + 1 for letter in input_string) % 2 != 0


print(is_odd_string('a'))  # True
print(is_odd_string('aaaa'))  # False
print(is_odd_string('amazing'))  # True
print(is_odd_string('veryfun'))  # True
print(is_odd_string('veryfunny'))  # False
