import re
n = input()

for i in range(int(n)):
    # Prompts the user for input string
    test = input()
    # compiling the pattern for alphanumeric string
    try:
        pat = re.compile(test)
        print(True)
    except:
        print(False)
