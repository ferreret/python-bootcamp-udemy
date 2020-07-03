'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

import csv


def delete_users(first, last):
    with open("users.csv") as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)

    print(rows)

    users_deleted = 0
    with open("users.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in rows:
            if row[0] == first and row[1] == last:
                users_deleted += 1
            else:
                csv_writer.writerow(row)

    return "Users deleted: {}".format(users_deleted)


print(delete_users("Grace", "Hopper"))
