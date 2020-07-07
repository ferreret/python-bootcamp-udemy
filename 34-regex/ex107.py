import re


def censor(input):
    pattern = re.compile(r"\bfrack[a-z]*\b", re.IGNORECASE)
    result = pattern.sub("CENSORED", input)
    return result


print(censor("Frack you"))
print(censor("I hope you fracking die"))
print(censor("you fracking Frack"))
