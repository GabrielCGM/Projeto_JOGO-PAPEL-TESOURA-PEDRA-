import os
import random
from time import sleep
import keyboard


class Jogador:

    #Função para sortear uma das opções.
    @classmethod
    def pc_escolha(cls):
        global escolha_comput,lista_op
        lista_op = ['\U0001F44A','\U0001F91A','\U0000270c']

        #escolhendo aleatorio uma jogada 
        escolha_comput = random.choice(lista_op)
        return escolha_comput

    #Method onde o jogador escolhe sua jogada.
    @classmethod
    def user_escolha(cls):
        global jog_escolha
        jog_escolha = print("""Pressione uma das teclas para escolher:

        [1]\U0001F44A
        [2]\U0001F91A
        [3]\U0000270c
""")

        #Captar a tecla que o jogador pressionou e seguir com suas respectivas ordens
        while True:
            try:
                
                if keyboard.is_pressed('one'):
                    jog_escolha = 1
                    print('SUA ESCOLHA>>>>> \U0001F44A')
                    break

                elif keyboard.is_pressed('two'):
                    jog_escolha = 2
                    print('SUA ESCOLHA>>>>> \U0001F91A')
                    break

                elif keyboard.is_pressed('three'):
                    jog_escolha = 3
                    print('SUA ESCOLHA>>>>> \U0000270c')
                    break

            except:
                continue
        return jog_escolha

    @classmethod
    def result_end(cls):
        print(f'MIHA ESCOLHA>>>>>',Jogador.pc_escolha())
        sleep(1)
        match jog_escolha:
            
            case 1:
                if escolha_comput == lista_op[0]:
                    print('EMPATE')
                elif escolha_comput == lista_op[1]:
                    print('Você perdeu!!!')
                else:
                    print('Você ganhou!!!')
            
            case 2:
                if escolha_comput == lista_op[1]:
                    print('EMPATE')
                elif escolha_comput == lista_op[2]:
                    print('Você perdeu!!!')
                else:
                    print('Você ganhou!!!')
            
            case 3:
                if escolha_comput == lista_op[2]:
                    print('EMPATE')
                elif escolha_comput == lista_op[0]:
                    print("Você perdeu!!!")
                else:
                    print("Você ganhou!!!")

    #Method utilit 
    @staticmethod
    def informacao():
        print("""
Como vai funcionar o jogo?
        
        Você escolhe entre uma das opções:
        [\U0001F44A] PEDRA
        [\U0001F91A] PAPEL
        [\U0000270c ] TESOURA

E vamos jogar :) Boa Sorte!""")

class Menu:
    os.system('cls')
    while True:
        menu_escolha = int(input("""
PRESSIONE UMA DAS TECLAS ABAIXO>>

        [1] INICIAR JOGO
        [2] Como funciona o jogo?
        [3] SAIR

Sua escolha>>>> """))

        #uso do match case para substituir if/elif
        match menu_escolha:
            case 1:
                Jogador.pc_escolha()
                Jogador.user_escolha()
                Jogador.result_end()

            case 2:
                Jogador.informacao()
                sleep(2)
                continue

            case 3:
                print('SAINDO....')
                sleep(1)
                break
        
                



