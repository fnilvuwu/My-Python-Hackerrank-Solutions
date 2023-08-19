

def product(fracs):
    t = reduce(lambda numerator, denominator : numerator*denominator ,fracs)
    return t.numerator, t.denominator

