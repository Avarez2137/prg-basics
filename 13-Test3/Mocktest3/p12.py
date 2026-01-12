import re

def f(dates):
    iso_pattern = r'\d{4}-\d{2}-\d{2}'
    return [date for date in dates.split(',') if re.match(iso_pattern, date)]
