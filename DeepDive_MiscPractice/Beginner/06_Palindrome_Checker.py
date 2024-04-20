import string

user_string = input('A string to check: ')
extra_chars = string.punctuation + ' ' + '’'

string_cleaning = filter(lambda a: a not in extra_chars and a, user_string)
cleaned_string = ''.join(list(string_cleaning)).lower()
reversed_string = ''.join(reversed(cleaned_string))

if cleaned_string == reversed_string:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
