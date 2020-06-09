numbers_1 = [1, 2, 3, 4]
numbers_2 = [3, 4, 5, 6]
answer = [number for number in numbers_1 if number in numbers_2]
print(answer)

words_1 = ["Elie", "Tim", "Matt"]
answer2 = [name[::-1].lower() for name in words_1]
print(answer2)
