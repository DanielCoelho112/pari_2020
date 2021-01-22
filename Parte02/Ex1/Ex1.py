# -*- encoding: utf-8 -*-
import sys

## main é o que corre quando o ficheiro é invocado

##tudo o que se define aqui é global


##O pydoc permite gerar um html com documentação sobre um módulo python partindo dos comentários inseridos em formato docstring.


##depois para criar basta ir a pasta do ficheiro e escrever pydoc -w ./














## isPrime é uma função auxiliar que vai returar true or false dependendo da natureza do numero
def isPerfect(value):
    """

    Aqui escrevemos o que a funçao faz
    :param value: escrevemos as entradas
    :return: escrevemos o que retorna
    """


    soma = 0
    for i in range(1,value):

        if value%i == 0:
            soma += i
    if soma == value:

        return  True
    else:
        return False


## % da o resto da divisao inteira






#print(isPrime(6))

def main():
     #for arg in sys.argv[1:]:
     #print(arg)

    maximum_number = int(sys.argv[1])


#range(n,m) começa no n, vai de 1 em 1, e acaba no m, excluindo m

    for j in range(1,maximum_number+1):
       if isPerfect(j):
           print("Number " + str(j) + " is Perfect")
       #else:
          # print("Number " + str(j) + " is not Prime")



#code to count the number of times that 3 appears in the prime numbers
 #python3 primos.py 10001 |grep "3" | wc -l




if __name__ == "__main__":
    main()