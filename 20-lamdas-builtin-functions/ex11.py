'''
names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
extract_full_name(names) # ['Elie Schoppik', 'Colt Steele']
'''


def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))


# def extract_full_name(names):
#     return list((person["first"] + " " + person["last"] for person in names))


names = [{'first': 'Elie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))  # ['Elie Schoppik', 'Colt Steele']
