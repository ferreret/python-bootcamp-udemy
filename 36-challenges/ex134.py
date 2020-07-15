'''
def add(a,b):
    return a+b

oneAddition = once(add)

oneAddition(2,2) # 4
oneAddition(2,2) # None
oneAddition(12,200) # None
'''


def once(func):
    count = 0

    def inner(a, b):
        nonlocal count
        if count == 0:
            count += 1
            return func(a, b)
        else:
            return None
    return inner


def add(a, b):
    return a+b


oneAddition = once(add)

print(oneAddition(2, 2))  # 4
print(oneAddition(2, 2))  # None
print(oneAddition(12, 200))  # None
