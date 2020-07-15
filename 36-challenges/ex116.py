'''
repeat('*', 3) # '***' 
repeat('abc', 2) # 'abcabc' 
repeat('abc', 0) # ''
'''


def repeat(input_string, number):
    result = ""
    for i in range(0, number):
        result += input_string
    return result


print(repeat('*', 3))  # '***'
print(repeat('abc', 2))  # 'abcabc'
print(repeat('abc', 0))  # ''
