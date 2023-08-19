

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        z1 = complex(self.real, self.imaginary)
        z2 = complex(no.real, no.imaginary)
        result = z1 + z2
        if result.imag > 0:
            return "{:.2f}+{:.2f}i".format(result.real, result.imag)
        elif result.imag == 0:
            return "{:.2f}+{:.2f}i".format(result.real, abs(result.imag))
        else:
            return "{:.2f}{:.2f}i".format(result.real, result.imag)

    def __sub__(self, no):
        z1 = complex(self.real, self.imaginary)
        z2 = complex(no.real, no.imaginary)
        result = z1 - z2
        if result.imag >= 0:
            return "{:.2f}+{:.2f}i".format(result.real, abs(result.imag))
        else:
            return "{:.2f}{:.2f}i".format(result.real, result.imag)

    def __mul__(self, no):
        z1 = complex(self.real, self.imaginary)
        z2 = complex(no.real, no.imaginary)
        result = z1 * z2
        if result.imag >= 0:
            return "{:.2f}+{:.2f}i".format(result.real, abs(result.imag))
        else:
            return "{:.2f}{:.2f}i".format(result.real, result.imag)

    def __truediv__(self, no):
        z1 = complex(self.real, self.imaginary)
        z2 = complex(no.real, no.imaginary)
        result = z1 / z2
        if result.imag >= 0:
            return "{:.2f}+{:.2f}i".format(result.real, abs(result.imag))
        else:
            return "{:.2f}{:.2f}i".format(result.real, result.imag)

    def mod(self):
        z1 = self.real
        z2 = self.imaginary
        result = complex(math.sqrt(z1**2+z2**2))
        if result.imag >= 0:
            return "{:.2f}+{:.2f}i".format(result.real, abs(result.imag))
        else:
            return "{:.2f}{:.2f}i".format(result.real, result.imag)


