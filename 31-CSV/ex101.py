'''
find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''

import csv
from csv import DictReader


def find_user(first_name, last_name):
    with open("users.csv") as csv_file:
        csv_reader = DictReader(csv_file)
        index = 1
        for row in csv_reader:
            if row["First Name"] == first_name and row["Last Name"] == last_name:
                return index
            index += 1
        return "Not Here not found."


print(find_user("Colt", "Steele"))  # 1
print(find_user("Alan", "Turing"))  # 3
print(find_user("Not", "Here"))  # 'Not Here not found.'


# Solución profe

# import csv
# def find_user(first_name, last_name):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         for (index, row) in enumerate(csv_reader):
#             first_name_match = first_name == row[0]
#             last_name_match = last_name == row[1]
#             if first_name_match and last_name_match:
#                 return index
#         return "{} {} not found.".format(first_name, last_name)
