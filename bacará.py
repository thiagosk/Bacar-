# Insper - Engenharia - Design de Software - Exercício Programa: Bacará Simplificado
# Thiago Shiguero Kawahara - Turma B - 10/2020

import random

pergunta = input("Gostaria de jogar Bacará? (s/n) ")
con = True
while con:
    if pergunta != "n" and pergunta != "s":
        pergunta = input("Gostaria de jogar Bacará? (s/n) ")
    else:
        con = False

if pergunta == "s":
    fdj = 100 #fichas do jogador
    print("Você tem {0} fichas.".format(fdj))

    fichas = int(input("Quantas fichas deseja apostar? "))
    c = True
    while c:
        if fichas > fdj:
            fichas = int(input("Fichas insuficientes. Quantas fichas deseja apostar? "))
        elif fichas == 0:
            fichas = int(input("Quantas fichas deseja apostar? "))
        else:
            c = False
    
    while fdj > 0 and pergunta == "s":

        aposta = input("Em quem irá apostar? (jogador/banco/empate) ")
        co = True
        while co:
            if aposta != "jogador" and aposta != "banco" and aposta != "empate":
                aposta = input("Em quem irá aposta? (jogador/banco/empate) ")
            else:
                co = False

        baralho = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"] * 8
        random.shuffle(baralho)

        print("Cartas do jogador: {0} e {1} ".format(baralho[0],baralho[1]))
        print("Cartas do banco: {0} e {1} ".format(baralho[2],baralho[3]))

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
            print("Nova carta do jogador: {0} ".format(baralho[4]))
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
            print("Nova carta do banco: {0} ".format(baralho[5]))
        else:
            None
            
        if valorjint > valorbint:
            print("Jogador ganhou!")
            if aposta == "jogador":
                fdj = fdj + fichas
            else:
                fdj = fdj - fichas
        elif valorjint < valorbint:
            print("Banco ganhou!")
            if aposta == "banco":
                fdj = fdj + (95/100 * fichas)
            else:
                fdj = fdj - fichas
        elif valorjint == valorbint:
            print("Empate!")
            if aposta == "empate":
                fdj = fdj + (8 * fichas)
            else:
                fdj = fdj - fichas
        print("Você esta com {0} fichas agora.".format(fdj))

        if fdj > 0:
            pergunta = input("Continuar jogando? (s/n) ")
            con = True
            while con:
                if pergunta != "n" and pergunta != "s":
                    pergunta = input("Continuar jogando? (s/n) ")
                else:
                    con = False
            if pergunta == "s":
                fichas = int(input("Quantas fichas deseja apostar? "))
                c = True
                while c:
                    if fichas > fdj:
                        fichas = int(input("Fichas insuficientes. Quantas fichas deseja apostar? "))
                    else:
                        c = False
            else:
                fichas == 0 #Somente uma condição para o while parar
    print("Obrigado por jogar!")

else:
    print("Sem problema.")

