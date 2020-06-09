'''
compact([0,1,2,"",[], False, {}, None, "All done"]) # [1,2, "All done"]
'''


def compact(input_list):
    return [item for item in input_list if item]


# [1,2, "All done"]
print(compact([0, 1, 2, "", [], False, {}, None, "All done"]))
