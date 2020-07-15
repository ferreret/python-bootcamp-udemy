'''
valid_parentheses("()") # True 
valid_parentheses(")(()))") # False 
valid_parentheses("(") # False 
valid_parentheses("(())((()())())") # True 
valid_parentheses('))((') # False
valid_parentheses('())(') # False
valid_parentheses('()()()()())()(') # False
'''


def valid_parentheses(parentheses):
    val = 0
    for p in parentheses:
        if p == "(":
            val += 1
        else:
            val -= 1
        if val < 0:
            return False
    return val == 0


print(valid_parentheses("()"))  # True
print(valid_parentheses(")(()))"))  # False
print(valid_parentheses("("))  # False
print(valid_parentheses("(())((()())())"))  # True
print(valid_parentheses('))(('))  # False
print(valid_parentheses('())('))  # False
print(valid_parentheses('()()()()())()('))  # False
