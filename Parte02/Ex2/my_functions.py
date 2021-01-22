def isPrime(value):

    for i in range(2,value):

        if  value%i == 0:
            return 0
    return 1

#  criar 2 ficheiros, 1 fica com funcoes e o outro nao
#para importartar from my_functions import getDividers, is Perfect
#ou
#import my fucntions
# e depois figo my_funtions.isPerfect(i)


#MELHOR MANEIRA

#import my_functions as mf

#e chamamos sempre mf