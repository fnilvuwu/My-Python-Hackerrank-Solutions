def wrapper(f):
    def fun(l):
        # complete the function
        l = sorted([x[len(x)-10:] if len(x)>10 else x for x in l])
        for i in l:
            print("+91", i[:5], i[5:])

    return fun
