'''
sum_pairs([4,2,10,5,1], 6) # [4,2]
sum_pairs([11,20,4,2,1,5], 100) # []
'''


def sum_pairs(input_list, number):
    for i in range(1, len(input_list)):
        if input_list[i] + input_list[i-1] == number:
            return [input_list[i-1], input_list[i]]
    return []


print(sum_pairs([4, 2, 10, 5, 1], 6))  # [4,2]
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))  # []
