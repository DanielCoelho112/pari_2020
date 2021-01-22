#! /usr/bin/env python


from collections import namedtuple
Complex = namedtuple('Complex', ['r', 'i'])





def addComplex(x, y):
    #x = numero complexo1
    #y = numero complexo 2

    #em vez de usar x[0] posso usar x.r

    real = x.r + y[0]

    imag = x[1] + y[1]
    out = Complex(real,imag)
    return out





def multiplyComplex(x, y):
    real = (x[0] * y[0]) - (x[1] * y[1])
    imag = (x[0] * y[1]) + (x[1] * y[0])
    out = Complex(real, imag)
    return out

def printComplex(x):
    print(str(x[0]) + "+" + str(x[1]) + "i")

def main():
    c1 = Complex(5, 3)  # use order when not naming
    c2 = Complex(i=7, r=-2)  # if items are names order is not relevant
    print('c1 = ' + str(c1))  # named tuple looks nice when printed

    # Test add
    c3=addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))


if __name__ == '__main__':
    main()