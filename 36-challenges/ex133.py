'''
counter = letter_counter('Amazing')
counter('a') # 2
counter('m') # 1

counter2 = letter_counter('This Is Really Fun!')
counter2('i') # 2
counter2('t') # 1 
'''


def letter_counter(input_string):
    reference_string = input_string.lower()

    def inner(letter):
        nonlocal reference_string
        return reference_string.count(letter.lower())
    return inner


counter = letter_counter('Amazing')
print(counter('a'))  # 2
print(counter('m'))  # 1

counter2 = letter_counter('This Is Really Fun!')
print(counter2('i'))  # 2
print(counter2('t'))  # 1
