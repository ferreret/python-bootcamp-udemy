f = open("story.txt")
print(f.read())
f.close()

with open("story.txt") as f2:
    f2.read()
