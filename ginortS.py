def myFunc(e):
    lowercase = []
    uppercase = []
    digit_odd = []
    digit_even = []
    for i in e:
        if i.isupper():
            uppercase.append(i)
        elif i.isdigit():
            if int(i) % 2 == 0:
                digit_even.append(i)
            else:
                digit_odd.append(i)
        else:
            lowercase.append(i)
    print("".join(sorted(lowercase) + sorted(uppercase) + sorted(digit_odd) + sorted(digit_even)))

s = list(input())

myFunc(s)
