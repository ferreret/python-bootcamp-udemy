def remove_negatives(numbers):
    return list(filter(lambda number: number >= 0, numbers))


print(remove_negatives([-1, 3, 4, -99]))
print(remove_negatives([-7, 0, 1, 2, 3, 4, 5]))
