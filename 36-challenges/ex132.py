'''
rAvg = running_average()
rAvg(10) # 10.0
rAvg(11) # 10.5
rAvg(12) # 11

rAvg2 = running_average()
rAvg2(1) # 1
rAvg2(3) # 2
'''


def running_average():
    count = 0
    sum_values = 0

    def inner(new_value):
        nonlocal count
        nonlocal sum_values
        count += 1
        sum_values += new_value
        return round(sum_values / count, 2)
    return inner


rAvg = running_average()
print(rAvg(10))  # 10.0
print(rAvg(11))  # 10.5
print(rAvg(12))  # 11

rAvg2 = running_average()
print(rAvg2(1))  # 1
print(rAvg2(3))  # 2
