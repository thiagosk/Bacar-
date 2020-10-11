# Insper - Engenharia - Design de Software - Exercício Programa: Bacará Simplificado
# Thiago Shiguero Kawahara - Turma B - 10/2020

import random

fdj = 100 #fichas do jogador
print("Você tem {0} fichas.".format(fdj))

fichas = int(input("Quantas fichas deseja apostar? "))
c = True
while c:
    if fichas > fdj or fichas < 0:
        fichas = int(input("Fichas insuficientes. Quantas fichas deseja apostar? "))
    else:
        c = False

fdj = fdj - fichas 
print("Você esta com {0} fichas agora.".format(fdj))

aposta = input("Em quem irá aposta? (jogador/banco/empate) ")
co = True
while co:
    if aposta != "jogador" and aposta != "banco" and aposta != "empate":
        aposta = input("Em quem irá aposta? (jogador/banco/empate) ")
    else:
        co = False

baralho = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K","A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
random.shuffle(baralho)
print(baralho) #APAGAR

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
if somajstr == "6" or somajstr == "7":
    somajstr = somajstr
    print("Valor(jogador): {0} ".format(valorj))
elif somajstr <= "5":
    novacartasj = []
    novacartasj.append(baralho[0])
    novacartasj.append(baralho[1])
    novacartasj.append(baralho[4])
    novasomaj = sum(novacartasj)
    novasomajstr = str(novasomaj)
    novovalorj = novasomajstr[len(novasomajstr)-1]
    print("Nova carta do jogador: {0}\nValor(jogador): {1} ".format(baralho[4],novovalorj))
else:
    print("Valor(jogador): {0} ".format(valorj))

cartasb = []
cartasb.append(baralho[2])
cartasb.append(baralho[3])
somab = sum(cartasb)
somabstr = str(somab)
valorb = somabstr[len(somabstr)-1]
if somabstr == "6" or somabstr == "7":
    somabstr = somabstr
    print("Valor(banco): {0} ".format(valorb))
elif somabstr <= "5":
    novacartasb = []
    novacartasb.append(baralho[2])
    novacartasb.append(baralho[3])
    novacartasb.append(baralho[5])
    novasomab = sum(novacartasb)
    novasomabstr = str(novasomab)
    novovalorb = novasomabstr[len(novasomabstr)-1]
    print("Nova carta do banco: {0}\nValor(banco): {1} ".format(baralho[5],novovalorb))
else:
    print("Valor(banco): {0} ".format(valorb))

#if valorj == 8 or valorj == 9 or valorb == 8 or valorb == 9: # CONDIÇAO PARA O JOGO ACABAR
#    if aposta == "jogador":
#        fdj = fdj + fichas
#    elif aposta == "banco":
#        fdj = fdj + (95/100 * aposta)
#    elif aposta == "empate":
#        fdj = fdj + (8 * aposta)



