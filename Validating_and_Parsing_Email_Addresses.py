# Enter your code here. Read input from STDIN. Print output to STDOUT
import email.utils
import re
for i in range(int(input())):
    parsed_email = email.utils.parseaddr(input())
    if re.match(r'^[a-zA-Z0-9]+[a-zA-Z0-9-._]+@[a-zA-Z]+\.[a-zA-Z]{1,3}$', parsed_email[1]):
        print(email.utils.formataddr(parsed_email))
