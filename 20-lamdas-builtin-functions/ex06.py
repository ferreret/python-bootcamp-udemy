def max_magnitude(numbers):
    return max(abs(num) for num in numbers)


print(max_magnitude([300, 20, -900]))
print(max_magnitude([10, 11, 12]))
print(max_magnitude([-5, -1, -89]))
