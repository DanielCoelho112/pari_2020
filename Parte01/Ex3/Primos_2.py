# -*- encoding: utf-8 -*-
#!/usr/bin/env python3


import sys


## main é o que corre quando o ficheiro é invocado

## tuple is immutable, list isnt
from colorama import Fore


def Divis(value):
    divisores = []

    for i in range(2, value):

        if value % i == 0:
            divisores.append(i)

    return divisores


# print(isPrime(6))

def main():
    # for arg in sys.argv[1:]:
    # print(arg)

    maximum_number = int(sys.argv[1])

    # range(n,m) começa no n, vai de 1 em 1, e acaba no m, excluindo m

    for j in range(1, maximum_number + 1):

        divi = Divis(j)

       # from colorama import Fore

        if not divi:
            print("Number " + Fore.GREEN +  str(j) + Fore.RESET + " is Prime, Divisores: " +
                  str(divi))
        else:
            # print("Number " + str(j) + " is not Prime, Divisores: " +
            #     ','.join([str(elem) for elem in divi]))
            print("Number " + str(j) + " is not Prime, Divisores: " +
                  str(divi))


if __name__ == "__main__":
    main()

# code to count the number of times that 3 appears in the prime numbers
# python3 primos.py 10001 |grep "3" | wc -l

