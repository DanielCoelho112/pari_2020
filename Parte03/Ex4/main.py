#! /usr/bin/python2.7

class Complex:
    """nesta classe encontram se todas as fucoes que dizem respeito aos complexos
    """

    def __init__(self, r, i):
        self.r = r  # store real part in class instance
        self.i = i  # store imaginary part in class instance

    def add(self, y):
        real = self.r + y.r
        imag = self.i + y.i
        return Complex(real, imag)

    def multiply(self, y):
        real = (self.r * y.r) - (self.i * y.i)
        imag = (self.r * y.i) + (self.i * y.r)
        return Complex(real,imag)

    def __str__(self):
        return (str(self.r) + "+" + str(self.i) + "i")







# instancia e objeto e a mesma coisa


def main():

    # declare two instances of class two complex numbers as tuples of size two
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant

    # Test add
    print(c1)  # uses the __str__ method in the class

    #fazendo apenas c1.add nao estou a fazer nada, pois nao estou a modificar o self na funcao, podia fazer isso, mas nao estou

    #c1.add(c2)
    c3 =Complex.add(c1,c2)
    print(c3)  # uses the __str__ method in the class

    # test multiply
    print(c2)  # uses the __str__ method in the class
    c10=c2.multiply(c1)
    print(c10)  # uses the __str__ method in the class

if __name__ == '__main__':
    main()