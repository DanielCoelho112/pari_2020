#! /usr/bin/python
from functools import partial


def main():



    def somar_3_val(a,b,c):
        return(a+b+c)


    #cria uma funcao, mas em que alguns dos elementos estao bloqueados
    sum_2_val =partial(somar_3_val,c=0)


    print(sum_2_val(2,3))



    #print(somar_3_val(3,2,0))



if __name__ == '__main__':
    main()