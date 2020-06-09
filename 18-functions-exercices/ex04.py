'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''


def number_compare(first, second):
    if first > second:
        return "First is greater"
    elif second > first:
        return "Second is greater"
    else:
        return "Numbers are equal"
