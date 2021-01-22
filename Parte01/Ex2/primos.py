# -*- encoding: utf-8 -*-

import sys

# main é o que corre quando o ficheiro é invocado

#tudo o que se define aqui é global


# isPrime é uma função auxiliar que vai returar true or false dependendo da natureza do numero
def isPrime(value):

    for i in range(2,value):

        if  value%i == 0:
            return 0
    return 1


# % da o resto da divisao inteira






#print(isPrime(6))

def main():
     #for arg in sys.argv[1:]:
     #print(arg)

    maximum_number = int(sys.argv[1])


#range(n,m) começa no n, vai de 1 em 1, e acaba no m, excluindo m

    for j in range(1,maximum_number+1):
       if isPrime(j):
           print("Number " + str(j) + " is Prime")
       #else:
          # print("Number " + str(j) + " is not Prime")



#code to count the number of times that 3 appears in the prime numbers
 #python3 primos.py 10001 |grep "3" | wc -l




if __name__ == "__main__":
    main()



