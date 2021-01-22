import readchar
import string


 #ord converte um character num inteiro  que e a posicao que esta

def printAllCharsUpTo(stop_char):

    #primeiro temos de ver a ordem do numero dado

    ordem = ord(stop_char)

    for i in range(32,ordem+1):
        print(chr(i))

def readAllUpTo(stop_char):

    #o que eu penso que e para fazer e o programa vai redebendo dados nossos e termina quando chegar ao carater X

    while True:
      key = readchar.readchar()
      print key
      if key == "X":
          break



def countNumbersUpto(stop_char):
    total_numbers = 0
    total_others = 0

    while True:
        key = readchar.readchar()
        print key

        if key.isdigit():
            total_numbers += 1
        else:
            total_others +=1

        if key == "X":

            break


    print('You entered ' + str(total_numbers) + ' numbers.')
    print('You entered ' + str(total_others) + ' others.')







def main():
    #key = readchar.readchar()
    #printAllCharsUpTo(key)
    #readAllUpTo("X")
    countNumbersUpto("X")


if __name__ == '__main__':
    main()



