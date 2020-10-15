# Insper - Engenharia - Design de Software - Exercício Programa: Bacará Simplificado
# Thiago Shiguero Kawahara - Turma B - 10/2020

import random

pessoas = int(input("Quantas pessoas gostariam de jogar? "))

fdj = 100 #fichas do jogador
listaf = [] #lista fichas dos jogadores
listafi = [] #lista fichas apostadas
listaa = [] #lista apostas

if pessoas > 0:
    contador = 1

    while pessoas > 0:

        x = listaf.count(0)
        i = 0
        while i < x:
            listaf.remove(0)
            listafi.remove(0)
            listaa.remove(0)
            i+=1

        if contador != 1:
            pessoas = len(listaf)
        else:
            None

        t=1
        while t <= pessoas:
            if contador == 1:
                listaf.append(fdj)
            else:
                None
            print("Jogador{0} tem {1} fichas.".format(t,listaf[t-1]))
            fichas = int(input("Quantas fichas deseja apostar jogador{0}? ".format(t)))

            c = True
            while c:
                if contador == 1:
                    if fichas > fdj:
                        fichas = int(input("Fichas insuficientes. Quantas fichas deseja apostar jogador{0}? ".format(t)))
                    elif fichas == 0:
                        fichas = int(input("Quantas fichas deseja apostar jogador{0}? ".format(t)))
                    else:
                        if contador == 1:
                            listafi.append(fichas)
                            c = False
                        else:
                            listafi[t-1] = fichas
                            c = False
                else:
                    if fichas > listaf[t-1]:
                        fichas = int(input("Fichas insuficientes. Quantas fichas deseja apostar jogador{0}? ".format(t)))
                    elif fichas == 0:
                        fichas = int(input("Quantas fichas deseja apostar jogador{0}? ".format(t)))
                    else:
                        if contador == 1:
                            listafi.append(fichas)
                            c = False
                        else:
                            listafi[t-1] = fichas
                            c = False

            t+=1 
        
        t=1
        while t <= pessoas:
            aposta = input("Em quem irá apostar jogador{0}? (jogador/banco/empate) ".format(t))
            co = True
            while co:
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
        
        baralho = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 4 * 8
        random.shuffle(baralho)

        print("Cartas do jogador: {0} e {1} ".format(baralho[0],baralho[1]))
        print("Cartas do banco: {0} e {1} ".format(baralho[2],baralho[3]))
        indice5 = baralho[4]
        indice6 = baralho[5]

        i = 0
        while i<len(baralho):
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

        cartasj = []
        cartasj.append(baralho[0])
        cartasj.append(baralho[1])
        somaj = sum(cartasj)
        somajstr = str(somaj)
        valorj = somajstr[len(somajstr)-1]
        valorjint = int(valorj)

        cartasb = []
        cartasb.append(baralho[2])
        cartasb.append(baralho[3])
        somab = sum(cartasb)
        somabstr = str(somab)
        valorb = somabstr[len(somabstr)-1]
        valorbint = int(valorb)

        if somajstr == "6" or somajstr == "7":
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

        if somabstr == "6" or somabstr == "7":
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

        if valorjint > valorbint:
            print("Jogador ganhou!")
        elif valorjint < valorbint:
            print("Banco ganhou!")
        elif valorjint == valorbint:
            print("Empate!")

        t=1
        while t <= pessoas:
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
        while t <= pessoas:
            print("Jogador{0} esta com {1} fichas agora. ".format(t,listaf[t-1]))
            t+=1

        listap = [] #lista pergunta
        t=1
        while t <= pessoas:
            if listaf[t-1] > 0:
                pergunta = input("Continuar jogando jogador{0}? (s/n) ".format(t))
                con = True
                while con:
                    if pergunta != "n" and pergunta != "s":
                        pergunta = input("Continuar jogando jogador{0}? (s/n) ".format(t))
                    else:
                        listap.append(pergunta)
                        if listap[t-1] == "n":
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
                print("Jogador{0} saiu.".format(t))
                listaf[t-1] = 0
                listafi[t-1] = 0
                listaa[t-1] = 0
                listap.append(0)
                t+=1

        x = listaf.count(0)
        i = 0
        while i < x:
            listaf.remove(0)
            listafi.remove(0)
            listaa.remove(0)
            i+=1

        pessoas = len(listaf)

        if pessoas > 0:
            print("Próxima rodada!")
            contador+=1
        else:
            print("Até a próxima.")

else:
    print("Sem problema.")



