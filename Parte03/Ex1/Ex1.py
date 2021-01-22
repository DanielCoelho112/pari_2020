# para baixar um reposiorio do git hub:
# git clone (url do repositorio)
import math
from colorama import  Fore
from time import time,ctime


#devolve o numero de segundos que passaram desde o inicio de uma epoca (tipicamente 1 de janeiro de 1970).

#devolve a data

def compute_sqrt(stop_number):
    for i in range(1,stop_number+1):
     x = math.sqrt(i)




def main():
    t1 = time()
    compute_sqrt(50000000)
    t2= time()
    print("This is " + Fore.RED + "Tutorial" + Fore.RESET + " and the current date is " + str(ctime()))
    print("Ellapsed time " + str(t2-t1) + " seconds")


if __name__ == "__main__":
    main()