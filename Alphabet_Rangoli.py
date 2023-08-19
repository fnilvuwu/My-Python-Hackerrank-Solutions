def print_rangoli(N):
    # your code goes here
    M = N*2 - 1

    list_char = []

    for i in range(N):
        list_char.append(chr(ord('a') + i))

    L = []
    for i in range(n):
        s = "-".join(list_char[i:n])
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(L[:0:-1]+L))

