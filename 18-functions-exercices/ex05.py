'''
single_letter_count("Hello World", "h") # 1
single_letter_count("Hello World", "z") # 0
single_letter_count("HelLo World", "l") # 3
'''

# define single_letter_count below:


def single_letter_count(string, letter):
    return string.upper().count(letter.upper())


print(single_letter_count("Hello World", "h"))
print(single_letter_count("Hello World", "z"))
print(single_letter_count("HelLo World", "l"))
