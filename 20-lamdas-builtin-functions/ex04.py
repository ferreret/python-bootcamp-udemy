def is_all_strings(iterable):
    return all(isinstance(item, str) for item in iterable)


print(is_all_strings(["a", "b", "c"]))
print(is_all_strings([2, "a", "b", "c"]))
