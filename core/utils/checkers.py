import re


def check_phone_number(phone):
    return bool(re.match(r'^8\d{10}$', phone))

