# don't forget to import re
import re
# define parse_bytes below:


def parse_bytes(input):
    pattern = re.compile(r"\b[01]{8}\b")
    return pattern.findall(input)
