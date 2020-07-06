# Don't forget to import re!
import re

# Define is_valid_time below:


def is_valid_time(time):
    pattern = re.compile(r"^\d{1,2}:\d{2}$")
    match = pattern.search(time)
    if match:
        return True
    return False
