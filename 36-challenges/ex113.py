'''
titleize('this is awesome') # "This Is Awesome"
titleize('oNLy cAPITALIZe fIRSt') # "ONLy CAPITALIZe FIRSt"
'''


def titleize(input_string):
    return " ".join(word[0].upper() + word[1:] for word in input_string.split(" "))


print(titleize('this i awesome'))  # "This Is Awesome"
print(titleize('oNLy cAPITALIZe fIRSt'))  # "ONLy CAPITALIZe FIRSt"
