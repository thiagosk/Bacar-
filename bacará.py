# Insper - Engenharia - Design de Software - Exercício Programa: Bacará Simplificado
    # Thiago Shiguero Kawahara - Turma B - 18/10/2020

import random

pessoas = int(input("Quantas pessoas gostariam de jogar? ")) #Pergunta quantas pessoas vão jogar

fdj = 100 #fichas iniciais de cada jogador
listaf = [] #lista que contêm a quantidade de fichas dos jogadores
listafi = [] #lista que contêm as fichas apostadas pelos jogadores
listaa = [] #lista que contêm em quem os jogadores apostaram (banco/jogador/empate)

if pessoas > 0: #o jogo só roda se tiver alguêm para jogar
    contador = 1 #ajuda no funcionamento do looping

    while pessoas > 0:

        x = listaf.count(0) #remove os jogadores que sairam 
        i = 0
        while i < x:
            listaf.remove(0)
            listafi.remove(0)
            listaa.remove(0)
            i+=1

        if contador != 1: #para todas as rodadas menos a primeira
            pessoas = len(listaf)
        else:
            None 

        t=1
        while t <= pessoas:
            if contador == 1: #somente para a primeira rodada
                listaf.append(fdj) #a lista começa vazia por isso tem que iniciar colocando os dados nela
            else: 
                None
            print("Jogador{0} tem {1} fichas.".format(t,listaf[t-1])) 
            fichas = int(input("Quantas fichas deseja apostar jogador{0}? ".format(t)))

            c = True
            while c: #caso as fichas apostadas sejam invalidas, o programa faz a pergunta novamente
                if contador == 1: #primeira rodada
                    if fichas > fdj:
                        fichas = int(input("Fichas insuficientes. Quantas fichas deseja apostar jogador{0}? ".format(t)))
                    elif fichas <= 0:
                        fichas = int(input("Quantas fichas deseja apostar jogador{0}? ".format(t)))
                    else:
                        listafi.append(fichas)
                        c = False
                else: #para as outras rodadas
                    if fichas > listaf[t-1]:
                        fichas = int(input("Fichas insuficientes. Quantas fichas deseja apostar jogador{0}? ".format(t)))
                    elif fichas <= 0:
                        fichas = int(input("Quantas fichas deseja apostar jogador{0}? ".format(t)))
                    else:
                        listafi[t-1] = fichas
                        c = False

            t+=1 
        
        t=1
        while t <= pessoas: #Pergunta em quem irá apostar
            aposta = input("Em quem irá apostar jogador{0}? (jogador/banco/empate) ".format(t))
            co = True
            while co: #Se a aposta for diferente das exigidas, perguta novamente
                if aposta != "jogador" and aposta != "banco" and aposta != "empate":
                    aposta = input("Em quem irá apostar jogador{0}? (jogador/banco/empate) ".format(t))
                else:
                    if contador == 1:
                        listaa.append(aposta)
                        co = False
                    else:
                        listaa[t-1] = aposta
                        co = False
            t+=1
        
        baralho = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 4 * 8 #baralho + embaralhar
        random.shuffle(baralho)

        print("Cartas do jogador: {0} e {1} ".format(baralho[0],baralho[1])) #mostra as cartas do jogador e da mesa
        print("Cartas do banco: {0} e {1} ".format(baralho[2],baralho[3]))
        indice5 = baralho[4]
        indice6 = baralho[5]

        i = 0
        while i<len(baralho): #troca strings do baralho para numeros para realizar as contas
            if baralho[i] == "A":
                baralho[i] = 1
                i+=1
            elif baralho[i] == 10 :
                baralho[i] = 0
                i+=1
            elif baralho[i] == "J":
                baralho[i] = 0
                i+=1
            elif baralho[i] == "Q":
                baralho[i] = 0
                i+=1
            elif baralho[i] == "K":
                baralho[i] = 0
                i+=1
            else:
                baralho[i] = baralho[i]
                i+=1

        cartasj = [] #fazer as contas das cartas do jogador
        cartasj.append(baralho[0])
        cartasj.append(baralho[1])
        somaj = sum(cartasj)
        somajstr = str(somaj) #para pegar o ultimo algarismo da soma
        valorj = somajstr[len(somajstr)-1] #pega o ultimo algarismo
        valorjint = int(valorj) #volta a ser um numero para fazer contas no futuro

        cartasb = [] #fazer as contas das cartas do banco
        cartasb.append(baralho[2])
        cartasb.append(baralho[3])
        somab = sum(cartasb)
        somabstr = str(somab) #para pegar o ultimo algarismo da soma
        valorb = somabstr[len(somabstr)-1] #pega o ultimo algarismo
        valorbint = int(valorb) #volta a ser um numero para fazer contas no futuro

        if somajstr == "6" or somajstr == "7": #condiçoes para entregar a terceira carta do jogador
            somajstr = somajstr
        elif somajstr <= "5" and somabstr != "8" and somabstr != "9":
            novacartaj = []
            novacartaj.append(baralho[0])
            novacartaj.append(baralho[1])
            novacartaj.append(baralho[4])
            novasomaj = sum(novacartaj)
            novasomajstr = str(novasomaj)
            valorj = novasomajstr[len(novasomajstr)-1]
            valorjint = int(valorj)
            print("Nova carta do jogador: {0} ".format(indice5))
        else:
            None

        if somabstr == "6" or somabstr == "7": #condiçoes para entregar a terceira carta para o banco
            somabstr = somabstr
        elif somabstr <= "5" and somajstr != "8" and somajstr != "9":
            novacartab = []
            novacartab.append(baralho[2])
            novacartab.append(baralho[3])
            novacartab.append(baralho[5])
            novasomab = sum(novacartab)
            novasomabstr = str(novasomab)
            valorb = novasomabstr[len(novasomabstr)-1]
            valorbint = int(valorb)
            print("Nova carta do banco: {0} ".format(indice6))
        else:
            None 

        if valorjint > valorbint: #mostrar o ganhador
            print("Jogador ganhou!")
        elif valorjint < valorbint:
            print("Banco ganhou!")
        elif valorjint == valorbint:
            print("Empate!")

        t=1
        while t <= pessoas: #pagamento das apostas
            if valorjint > valorbint:
                if listaa[t-1] == "jogador":
                    listaf[t-1] = listaf[t-1] + listafi[t-1] 
                else:
                    listaf[t-1] = listaf[t-1] - listafi[t-1]
            elif valorjint < valorbint:
                if listaa[t-1] == "banco":
                    listaf[t-1] = listaf[t-1] + (95/100 * listafi[t-1])
                else:
                    listaf[t-1] = listaf[t-1] - listafi[t-1]
            elif valorjint == valorbint:
                if listaa[t-1] == "empate":
                    listaf[t-1] = listaf[t-1] + (8 * listafi[t-1])
                else:
                    listaf[t-1] = listaf[t-1] - listafi[t-1]
            t+=1
            
        t=1
        while t <= pessoas: #falar quanto cada jogador tem dps das aposta
            print("Jogador{0} esta com {1} fichas agora. ".format(t,listaf[t-1]))
            t+=1

        listap = [] #lista que contêm as respostas(n ou s)
        t=1
        while t <= pessoas:
            if listaf[t-1] > 0:
                pergunta = input("Continuar jogando jogador{0}? (s/n) ".format(t))
                con = True
                while con: #se a resposta for direfente de "n" ou "s", pergutan dnv
                    if pergunta != "n" and pergunta != "s":
                        pergunta = input("Continuar jogando jogador{0}? (s/n) ".format(t))
                    else:
                        listap.append(pergunta)
                        if listap[t-1] == "n": #zerar os valores da lista do jogador que disse "nao" para facilitar sua remoçao do jogo
                            print("Jogador{0} saiu.".format(t))
                            listaf[t-1] = 0
                            listafi[t-1] = 0
                            listaa[t-1] = 0
                            listap[t-1] = 0
                            t+=1
                        else:
                            t+=1
                        con = False
            else:
                print("Jogador{0} saiu.".format(t)) #zerar os valores da lista do jogador que ta com 0 fichas para facilitar sua remoçao do jogo
                listaf[t-1] = 0
                listafi[t-1] = 0
                listaa[t-1] = 0
                listap.append(0)
                t+=1

        x = listaf.count(0) #remover as pessoas do jogo
        i = 0
        while i < x:
            listaf.remove(0)
            listafi.remove(0)
            listaa.remove(0)
            i+=1

        pessoas = len(listaf) #atualizar a quantidade de jogadores

        if pessoas > 0: #fala se o jogo continua ou acaba dependendo da quantidade de jogadores
            print("Próxima rodada!")
            contador+=1
        else:
            print("Até a próxima.")

else: #sem jogadores iniciais, o jogo nem roda
    print("Sem problema.")



