
# flesh out intersection pleaseeeee


def intersection(list1, list2):
    return list(set([item for item in list1 if list2.count(item) > 0]))


print(intersection([1, 2, 3], [2, 3, 4]))
print(intersection(["a", "b", "z"], ["x", "y", "z"]))
