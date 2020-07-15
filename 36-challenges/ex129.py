'''
reverse_vowels("Hello!") # "Holle!" 
reverse_vowels("Tomatoes") # "Temotaos" 
reverse_vowels("Reverse Vowels In A String") # "RivArsI Vewols en e Streng"
reverse_vowels("aeiou") # "uoiea"
reverse_vowels("why try, shy fly?") # "why try, shy fly?"
'''


def reverse_vowels(input_string):
    vowels = "aeiou"
    vowels_in_input = list(reversed(
        [char for char in input_string if char.lower() in vowels]))
    index = 0
    result = ""
    for char in input_string:
        if char.lower() in vowels:
            result += vowels_in_input[index]
            index += 1
        else:
            result += char
    return result


print(reverse_vowels("Hello!"))  # "Holle!"
print(reverse_vowels("Tomatoes"))  # "Temotaos"
# "RivArsI Vewols en e Streng"
print(reverse_vowels("Reverse Vowels In A String"))
print(reverse_vowels("aeiou"))  # "uoiea"
print(reverse_vowels("why try, shy fly?"))  # "why try, shy fly?"
