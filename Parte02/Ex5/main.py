
import readchar
import string


# ord converte um character num inteiro  que e a posicao que esta

def printAllCharsUpTo(stop_char):
    # primeiro temos de ver a ordem do numero dado

    ordem = ord(stop_char)

    for i in range(32, ordem + 1):
        print(chr(i))


def readAllUpTo(stop_char):
    # o que eu penso que e para fazer e o programa vai redebendo dados nossos e termina quando chegar ao carater X

    while True:
        key = readchar.readchar()
        print key
        if key == "X":
            break


def countNumbersUpto(stop_char):
    inputs = []

    while True:

        key = readchar.readchar()
        print key
        inputs.append(key)

        if key == stop_char:
            break

    total_numbers = 0
    total_others = 0

    lista_num = []
    dic_other = {}
    ordem = 0
    for input in inputs:
        ordem += 1

        # process each input in the list

        if input.isdigit():
            total_numbers += 1
            lista_num.append(input)

        else:
            total_others += 1
            dic_other[ordem]=input



    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')
    print ('Numerical list:' + str(lista_num))
    lista_num.sort()
    print ('Dictionaty with other:' + str(dic_other))
    print ('Ordered numerical list :' + str(lista_num))
    #print the first input non number
    #print (dic_other[1])

def countNumbersUpto_Al_e(stop_char):

    inputs = []

    while True:

        key = readchar.readchar()
        print key
        inputs.append(key)

        if key == stop_char:
            break

    #list comprehension: [expression for item in list if conditional]

    numerical_list = [input for input in inputs if input.isdigit()]
    print str(numerical_list)


def main():
     key = readchar.readchar()
     printAllCharsUpTo(key)
    # readAllUpTo("X")
    #countNumbersUpto("X")
    #countNumbersUpto_Al_e("X")



if __name__ == '__main__':
    main()

