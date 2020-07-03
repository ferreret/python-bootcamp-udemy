'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''


def get_multiples(number=1, count=10):
    for counter in range(0, count):
        yield (counter + 1) * number


evens = get_multiples(2, 3)
print(next(evens))  # 2
print(next(evens))  # 4
print(next(evens))  # 6
print(next(evens))  # StopIteration

default_multiples = get_multiples()
print(list(default_multiples))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
