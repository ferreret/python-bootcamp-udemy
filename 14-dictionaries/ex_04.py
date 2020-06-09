# This code picks a random food item:
from random import choice  # DON'T CHANGE!
food = choice(["cheese pizza", "quiche", "morning bun",
               "gummy bear", "tea cake"])  # DON'T CHANGE!

# DON'T CHANGE THIS DICTIONARY EITHER!
bakery_stock = {
    "almond croissant": 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}

print(food)
# YOUR CODE GOES BELOW:
no_items_stock = bakery_stock.get(food)

if no_items_stock:
    print("{} left".format(str(no_items_stock)))
else:
    print("We don't make that")
