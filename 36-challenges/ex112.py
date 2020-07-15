'''
vowel_count('awesome') # {'a': 1, 'e': 2, 'o': 1}
vowel_count('Elie') # {'e': 2, 'i': 1}
vowel_count('Colt') # {'o': 1}
'''


def vowel_count(input_string):
    # vowels = ("a", "e", "i", "o", "u")
    # result = {}

    # for char in input_string.lower():
    #     if char in vowels:
    #         result[char] = result.get(char, 0) + 1

    # return result
    lower_s = input_string.lower()
    return {letter: lower_s.count(letter) for letter in lower_s if letter in "aeiou"}


print(vowel_count('awesome'))  # {'a': 1, 'e': 2, 'o': 1}
print(vowel_count('Elie'))  # {'e': 2, 'i': 1}
print(vowel_count('Colt'))  # {'o': 1}
