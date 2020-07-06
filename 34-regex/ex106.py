import re

# define parse_date below


def parse_date(input):
    pattern = re.compile(r"^(?P<d>\d{2})[./,](?P<m>\d{2})[./,](?P<y>\d{4})$")
    matches = pattern.search(input)

    if matches:
        return {"d": matches.group("d"),
                "m": matches.group("m"),
                "y": matches.group("y")}
    return None


print(parse_date("22/3/1974"))
