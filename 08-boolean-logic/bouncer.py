# Ask for age
print("How old are you:")
age = input()
age = int(age)

if age >= 21:
    # 21+ drink, normal entry
    print("You are good to enter and drink")
elif age >= 18:
    # 18 - 21 wristband
    print("You can enter, but show your wristband")
else:
    # too young, sorry
    print("You can't enter")
