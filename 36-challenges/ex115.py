
'''
includes([1, 2, 3], 1) # True 
includes([1, 2, 3], 1, 2) # False 
includes({ 'a': 1, 'b': 2 }, 1) # True 
includes({ 'a': 1, 'b': 2 }, 'a') # False
includes('abcd', 'b') # True
includes('abcd', 'e') # False
'''


def includes(collection, value, start_index=0):
    if (isinstance(collection, dict)):
        return any(x == value for x in collection.values())
    return any(x == value for x in collection[start_index:])


print(includes([1, 2, 3], 1))  # True
print(includes([1, 2, 3], 1, 2))  # False
print(includes({'a': 1, 'b': 2}, 1))  # True
print(includes({'a': 1, 'b': 2}, 'a'))  # False
print(includes('abcd', 'b'))  # True
print(includes('abcd', 'e'))  # False
