import re
t = int(input())
for i in range(t):
    s = input()
    no_char_repeat = re.match(r'^(?!.*(.).*\1)\w+$', s)
    two_uppercase = re.match(r"^(.*?[A-Z]){2,}.*$", s)
    three_digit = re.match(r"^(.*?[0-9]){3,}.*$", s)
    alpha_numeric = re.match(r"\w+", s)
    length_ten = re.match(r"^.{10}$", s)

    if(no_char_repeat and two_uppercase and three_digit and alpha_numeric and length_ten):
        print("Valid")
    else:
        print("Invalid")
