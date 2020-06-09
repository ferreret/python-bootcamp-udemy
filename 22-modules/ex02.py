from keyword import iskeyword


def contains_keyword(*args):
    return any(iskeyword(arg) for arg in args)


print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol", "chicken", "alaska"))
print(contains_keyword("four", "for", "if"))
print(contains_keyword("blah", "doggo", "crab", "anchor"))
print(contains_keyword("arizzlv", "ianore", "return", "False"))
