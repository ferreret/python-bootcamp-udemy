'''
print_users()  # None
# prints to the console:
# Colt Steele
'''

from csv import DictReader


def print_users():
    with open("users.csv") as csv_file:
        csv_reader = DictReader(csv_file)
        for row in csv_reader:
            print("{} {}".format(row["First Name"], row["Last Name"]))


print_users()
