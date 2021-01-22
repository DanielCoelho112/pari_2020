#!/usr/bin/env python
# coding=utf-8
import argparse
import random
import readchar
from time import *
from collections import namedtuple
from colorama import Fore
from pprint import pprint

Input = namedtuple('Input', ['Requested', 'Received', 'Duration'])

start = 0  # Define a variavel global


def tic():
    global start
    start = time()
    return time()


def toc():
    global start
    delta_t = time() - start
    return delta_t


# -------------------------------------NOVAS CLASSES ----------------------------------------

class estatisticaJogador():

    def __init__(self):
        self.dict={'test_duration': None,
                   'inputs': None,
                   'test_start': ctime(),                  # Data do inicio do jogo e atribui
                   'test_end': None,                       # Inicia data do fim do teste mas não atribui
                   'number_of_types': 0,                   # Inicia a variavel a 0
                   'number_of_hits': 0,                    # Inicia a variavel a 0
                   'accuracy': None,                          # Calculo da pericia
                   'type_average_duration': 0,             # Duranção media das respostas
                   'type_hit_average_duration': 0,         # duração média das respostas corretas do utilizador
                   'type_miss_average_duration': 0         # duração média das respostas incorretas do utilizador
                   }

        self.incrementoDeTempoErrados =0                         # Inicia a variavel a 0

    def setTempoDeJogo(self, tempojogo):
        self.dict['test_duration'] = tempojogo                            # Recebe por atribuição o tempo de jogo final

    def setDataFimTeste(self,dataFimTeste):
        self.dict['test_start']=dataFimTeste                     # Recebe por atribuição a data final do teste

    def incrementarInput(self):
        self.dict['number_of_types'] += 1

    def incrementDuration(self,duracao):
        self.dict['type_average_duration']+=duracao

    def incrementDurationhitsCertos(self,duracao):
        self.dict['type_hit_average_duration']+=duracao
    def incrementarDuracaoHitErrados(self,duracao):
        self.incrementoDeTempoErrados += duracao

    def incrementarHitsCertos(self):
            self.dict['number_of_hits'] += 1

    def getInputs(self, inputs):
        self.dict['inputs'] = inputs

    #Controi a string de escrita
    def getStringSaida(self):

        #Calculo do acuracy
        hits = float(self.dict['number_of_hits'])
        types = float(self.dict['number_of_types'])
        self.dict['accuracy'] = hits/types   # Atualiza accuracy
        #Calcula final da duração media
        if self.dict['number_of_types']:             #Porque se for 0 da erro
            self.dict['type_average_duration'] = self.dict['type_average_duration']/self.dict['number_of_types']
        # Calcula final da duração media hits certos
        if self.dict['number_of_hits']:             #Porque se for 0 da erro
            self.dict['type_hit_average_duration'] = self.dict['type_hit_average_duration'] / self.dict['number_of_hits']
        if self.incrementoDeTempoErrados>0:         #Porque se for 0 da erro
            self.dict['type_miss_average_duration']= self.incrementoDeTempoErrados/ (self.dict['number_of_types']-self.dict['number_of_hits'])
        self.dict['test_end'] = ctime()

        return self.dict


class timer():
    def __init__(self):
        self.start = 0
        self.delta_t = 0

    def tic(self):
        self.start = time()
        return time()

    def toc(self):
        self.delta_t = time() - self.start
        return self.delta_t

    def getDelta_t(self):
        return self.delta_t


# -------------------------------------NOVAS CLASSES ----------------------------------------

# funcao que gera automaticamente uma letra aleatoria

def random_letter():
    letter = chr(random.randrange(97, 122, 1))
    return letter


def main():
    ##---------------------------PARTE DE TRATAMENTO DOS ARGUMENTOS E DEFINICAO DO MODO DE JOGO----------------------------------##

    ap = argparse.ArgumentParser(description='Definition of a test mode:')
    ap.add_argument('-utm', '--use_time_mode', action='store_const', const=True, default=False,
                    help='Max number of secs for time mode or maximum number of inputs for number of inputs mode.')

    ap.add_argument('-mv', '--max_value', type=int, default=20,
                    help=' Max number of seconds for time mode or maximum number of inputs for number of inputs mode.')
    args = vars(ap.parse_args())

    # Variáveis de nº de tentativas e do tempo de jogo
    mv = args['max_value']
    utm = args['use_time_mode']

    # verificacao se o utilizador cumpriu os requisistos de jogo

    if mv <= 0:
        print("Max number of seconds for time or maximum number of inputs missing!")
        print("Please type './main.py -h' and check the instructions")
        return

    print(args)

    # -----Escolha dos Modos-----

    # Mode_Setup = 0 ---------- Tempo de jogo
    # Mode_Setup = 1 ---------- Nº tentativas

    Mode_Setup = 0

    # Modo - Tempo de jogo
    if utm == True:
        Mode_Setup = 0

    # Modo - Nº tentativas
    if utm == False:
        Mode_Setup = 1

    ##---------------------------PARTE DE CRIACAO DO CICLO DO JOGO----------------------------------##

    print (Fore.RED + "PARI " + Fore.RESET + "Typing Test, Daniel Coelho, Luís Dias, Samuel Ferreira, October 2020")

    # mensagem que mostra qual o tipo de jogo que irá ser jogado

    if Mode_Setup == 0:
        print ("Test running up to " + str(mv) + " seconds.")
    else:
        print ("Test running up to " + str(mv) + " inputs.")

    # mensagem que dá origem ao inicio do jogo caso o utilizador pressione alguma tecla

    temporizadorJogo = timer()  # Adiciona um objeto do tipo timer

    print ("Press any key to start the test")

    first_key = readchar.readchar()

    # inicia o contador Start
    temporizadorJogo.tic()  # Inicia a contagem do tempo de jogo
    statsJogador=estatisticaJogador()
    ordem = 0
    dict_input = {}

    while True:

        # ordem da jogava vai incrementando uma unidade para se ir criando a dict_input consoante a jogada
        ordem += 1
        statsJogador.incrementarInput()                                  # Incrementa hits nas estatisticas

        # inicio da jogada em questao
        inicio_jogada = time()

        # letra minuscula gerada automaticamente
        requested = random_letter()

        print ("Type letter " + Fore.BLUE + requested + Fore.RESET)

        # letra recebida
        received = readchar.readchar()

        # duracao da jogada em questao
        duration = time() - inicio_jogada

        # se o caracter recebido for 'space' (chr(32)) o jogo da se por terminado

        if received == chr(32):
            print(Fore.RED + "You gave up LOSER" + Fore.RESET)
            temporizadorJogo.toc()
            break

        # verificar se o utilizador acertou ou nao
        if requested == received:
            statsJogador.incrementarHitsCertos()                                # Se acertar incrementa nos hits certos
            statsJogador.incrementDurationhitsCertos(duration)
            print ("You typed letter " + Fore.GREEN + received + Fore.RESET)
        else:
            statsJogador.incrementarDuracaoHitErrados(duration)
            print ("You typed letter " + Fore.RED + received + Fore.RESET)

        # Guardar a letra requested,received and duration na namedtupled (Tuple_Input) para posteriormente colocar na
        # dict_input
        statsJogador.incrementDuration(duration)                                 # Incrementa a duranção
        Tuple_Input = Input(Requested=requested, Received=received, Duration=duration)

        # Guardar a informacao da jogada numa dict, a chave da dict é a ordem do input, e o seu valor é uma
        # namedtuple que contem a letra requested,received and duration
        dict_input[ordem] = Tuple_Input

        # Aqui tem que se ver se o jogo acabou ou nao


        if Mode_Setup == 0 and temporizadorJogo.toc() >= mv:
            print ("Current test duration (" + str(temporizadorJogo.toc()) + "s) seconds exceeds maximum of " + str(mv) + " seconds")
            temporizadorJogo.toc()
            print (Fore.BLUE + "Test finished!" + Fore.RESET)
            break

        if Mode_Setup == 1 and ordem == mv:
            print ("Current number of inputs reaches maximum of " + str(mv))
            temporizadorJogo.toc()
            print (Fore.BLUE + "Test finished!" + Fore.RESET)
            break

    ##---------------------------TRATAMENTO DA INFORMACAO CONTIDA NA dict_input------------------------------------##
    statsJogador.setTempoDeJogo(temporizadorJogo.getDelta_t())          # Recebe o tempo de jogo final.
    statsJogador.setDataFimTeste(ctime())                               # Atribui a data final do teste
    statsJogador.getInputs(dict_input)

    pprint(statsJogador.getStringSaida())     #Recebe o dicionario total das estatisticas e mostra na tela


if __name__ == "__main__":
    main()
