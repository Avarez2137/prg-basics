import re

def f(mnumbers):
    valid_pattern = r'^[+-]?[1-7a-d]+$'
    return sum(1 for mn in mnumbers if re.match(valid_pattern, mn, re.IGNORECASE))
