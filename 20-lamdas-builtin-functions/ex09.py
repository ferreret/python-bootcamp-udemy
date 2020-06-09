def interleave(param1, param2):
    return "".join("".join(pair) for pair in zip(param1, param2))


print(interleave("hi", "ha"))
print(interleave("aaa", "zzz"))
print(interleave("lzr", "iad"))
