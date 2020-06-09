'''
list_manipulation([1,2,3], "remove", "end") # 3
list_manipulation([1,2,3], "remove", "beginning") #  1
list_manipulation([1,2,3], "add", "beginning", 20) #  [20,1,2,3]
list_manipulation([1,2,3], "add", "end", 30) #  [1,2,3,30]
'''


def list_manipulation(lista, command, location, value=None):
    if command == "remove" and location == "end":
        return lista.pop()
    elif command == "remove" and location == "beginning":
        return lista.pop(0)
    elif command == "add" and location == "beginning":
        lista.insert(0, value)
        return lista
    elif command == "add" and location == "end":
        lista.append(value)
        return lista


print(list_manipulation([1, 2, 3], "remove", "end"))  # 3
print(list_manipulation([1, 2, 3], "remove", "beginning"))  # 1
print(list_manipulation([1, 2, 3], "add", "beginning", 20))  # [20,1,2,3]
print(list_manipulation([1, 2, 3], "add", "end", 30))  # [1,2,3,30]
