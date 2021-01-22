

#tuple para definir o numero complexo, tuple(1)=real and tuple(2) = imag

def addComplex(x, y):
    #x = numero complexo1
    #y = numero complexo 2
    real = x[0] + y[0]
    imag = x[1] + y[1]
    out = (real,imag)
    return out





def multiplyComplex(x, y):
    real = (x[0] * y[0]) - (x[1] * y[1])
    imag = (x[0] * y[1]) + (x[1] * y[0])
    out = (real, imag)
    return out

def printComplex(x):
    print(str(x[0]) + "+" + str(x[1]) + "i")

def main():
    # define two complex numbers as tuples of size two
    c1 = (5, 3)
    c2 = (-2, 7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))




if __name__ == '__main__':
    main()