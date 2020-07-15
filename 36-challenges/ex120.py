'''
same_frequency(551122,221515) # True
same_frequency(321142,3212215) # False
same_frequency(1212, 2211) # True
'''


def same_frequency(num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    dict1 = {letter: num1.count(letter) for letter in num1}
    dict2 = {letter: num2.count(letter) for letter in num2}
    return dict1 == dict2


print(same_frequency(551122, 221515))  # True
print(same_frequency(321142, 3212215))  # False
print(same_frequency(1212, 2211))  # True
