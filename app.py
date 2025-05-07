def is_valid_email(email):
    return "@" in email and "." in email

def add(a, b):
    return a + b

def get_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

def reverse_date(date_str):
    parts = date_str.split("-")
    return f"{parts[2]}.{parts[1]}.{parts[0]}"

def is_palindrome(word):
    cleaned = word.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
