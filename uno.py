import random
import time
cores = ['verde','vermelho','amarelo','azul']
numeros = [' 0',' 1',' 2',' 3',' 4',' 5',' 6',' 7',' 8',' 9']
especiais = [' comprar duas',' inverter',' pular']
coringas = ['coringa comprar quatro','coringa']
jogadores = []
baralhos = []
jogada = []
def baralho():
    baralho = []
    for cor in cores:
        for numero in numeros:
            baralho.append(cor+numero)
            if numero!=' 0':
                baralho.append(cor+numero)
        for especial in especiais:
            baralho.append(cor+especial)
            baralho.append(cor+especial)
        for coringa in coringas:
            baralho.append(coringa)
    return baralho

def embaralhar(deck):
    random.shuffle(deck)

def distribuir(deck):
    cartas = []
    for i in range(7):
        cartas.append(deck[i])
        deck.remove(deck[i])
    return cartas

def comprarCarta(deck): 
    carta = deck.pop(0)
    return carta

def distribuirJogo(qtJogadores,deck):
    if qtJogadores<2:
        print("Quantidade mínima de dois jogadores!!")
    else:
        for n in range(qtJogadores):
            print("Digite o nome do jogador %d" %(n+1))
            jogadores.append(input())
            baralhos.append(distribuir(deck))

def inverter(quemJoga):
    quemE = jogadores[quemJoga]
    jogadores.reverse() 
    quemJoga = proximoJogador(jogadores.index(quemE))
    baralhos.reverse()
    return quemJoga

def coringa():
    cor = random.choice(cores)
    return "Jogador jogou um coringa e escolheu a cor "+cor

def proximoJogador(quemJoga):
    if quemJoga == len(jogadores)-1:
        quemJoga = 0
    else:
        quemJoga+=1
    return quemJoga

def verificaCarta(carta):
    card = carta.split(' ')
    if card[0] == 'coringa':
        if len(card) == 1:   
            return "coringa"
        else:
            return "quatro"
    elif card[1] == 'inverter':      
        return "inverter"
    elif card[1] == 'pular':
        return "pular"
    elif len(card) == 3:
        return "duas"
    else:
        return "normal"

def verSeTemDoisOuQuatro(baralho):
    jogada = []
    for carta in baralho:
        tipoCarta = verificaCarta(carta)
        if tipoCarta == "duas" or tipoCarta == "quatro":
            jogada.append(carta)
    return jogada
            
def verSeTemQuatro(baralho):
    jogada = []
    for carta in baralho:
        tipoCarta = verificaCarta(carta)
        if tipoCarta == "quatro":
            jogada.append(carta)
    return jogada
            
def verSeTemCorOuNumero(baralho,cartaTopo):
    jogada = []
    cartaBaralho = cartaTopo.split(' ')
    for carta in baralho: 
        cartaJogador = carta.split(' ')  
        if cartaJogador[0] == 'coringa':
           jogada.append(carta)
        elif cartaJogador[0] == cartaBaralho[0] or cartaJogador[1] == cartaBaralho[1]:
           jogada.append(carta)
    return jogada
def test():
    assert verificaCarta('coringa comprar quatro') == 'duas'

def main():
    deck = []
    puxar = []
    quemJoga = 0
    rodada = 1
    cor = ''
    puxarQuantas = 0
    jaFoi = False
    descarte = []
    deck = baralho()
    embaralhar(deck)
    print('='*60)
    print('UNO'.center(60))
    print('='*60)
    qtJogadores = int(input('Quantos Jogadores? '))
    distribuirJogo(qtJogadores,deck)
    cartaTopo = comprarCarta(deck)
    ganhou = False
    marcaRodada = 0

    while ganhou != True:
        print("Rodada ",rodada)
        jogada = []
        print('='*60)
        print("Carta no topo: ",cartaTopo)
        card = cartaTopo.split(' ')
        #if card[0]== 'coringa':
        descarte.append(cartaTopo)
        #elif card[1] != '-':
        #    descarte.append(cartaTopo)
        tipoCarta = verificaCarta(cartaTopo)
        if marcaRodada == rodada:
            puxarQuantas = 0
            jaFoi = False
        if rodada == 1:
            if tipoCarta == "quatro":
                cartaTopo = comprarCarta(deck)
                continue
            elif tipoCarta == "coringa":
                cor = random.choice(cores)
                print("jogador escolheu a cor",cor)
                cartaTopo = cor + ' -'
                jogada = verSeTemCorOuNumero(baralhos[quemJoga],cartaTopo)
                if len(jogada)>0:
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    print("Opções para jogar: ",jogada)    
                    jogar = random.choice(jogada)
                    cartaTopo = jogar
                    verificaCarta(cartaTopo)
                    baralhos[quemJoga].remove(jogar)
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    
                else:
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    puxar.append(comprarCarta(deck))
                    print ("Puxou a carta: ",puxar)
                    jogada = verSeTemCorOuNumero(puxar,cartaTopo)
                    if len(jogada)>0:
                        cartaTopo = puxar[0]
                        print ("Jogou ",puxar[0])
                        verificaCarta(cartaTopo)
                    else:
                        baralhos[quemJoga].append(puxar[0])
                        print("pegou  ",baralhos[quemJoga])
                    puxar.clear()
                quemJoga = proximoJogador(quemJoga)
                rodada+=1
                jogada = []
                continue
        if tipoCarta == "coringa":
            cor = random.choice(cores)
            print("jogador escolheu a cor",cor)
            cartaTopo = cor + ' -'
            continue
        if tipoCarta == "pular":
            if jaFoi== False:
                print("Carta 'pular' foi utilizada, passou a vez do jogador ",jogadores[quemJoga])
                jaFoi = True
                marcaRodada = rodada+2
                jogada = []
                
            else:
                jaFoi == False
                jogada = verSeTemCorOuNumero(baralhos[quemJoga],cartaTopo)
                if len(jogada)>0:
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    print("Opções para jogar: ",jogada)    
                    jogar = random.choice(jogada)
                    cartaTopo = jogar
                    print("Jogou : ", jogar)
                    verificaCarta(cartaTopo)
                    baralhos[quemJoga].remove(jogar)
                    jogada = []
                    
                else:
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    puxar.append(comprarCarta(deck))
                    print ("Puxou a carta: ",puxar)
                    jogada = verSeTemCorOuNumero(puxar,cartaTopo)
                    if len(jogada)>0:
                        cartaTopo = puxar[0]
                        print("Jogou ",puxar)
                        verificaCarta(cartaTopo)
                    else:
                        baralhos[quemJoga].append(puxar[0])
                        print("pegou  ",baralhos[quemJoga])
                    puxar.clear()
                    jogada = []
            #rodada+=1
            jogada = []
                
            
        elif tipoCarta == "inverter":
            if jaFoi == False:
                quemJoga = inverter(quemJoga)
                print("Jogada invertida, é a vez do jogador ",jogadores[proximoJogador(quemJoga)])
                jaFoi = True
                marcaRodada = rodada+2
                jogada = []
                
            else:
                jaFoi == False
                jogada = verSeTemCorOuNumero(baralhos[quemJoga],cartaTopo)
                if len(jogada)>0:
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    print("Opções para jogar: ",jogada)    
                    jogar = random.choice(jogada)
                    cartaTopo = jogar
                    print("Jogou : ", jogar)
                    verificaCarta(cartaTopo)
                    baralhos[quemJoga].remove(jogar)
                    jogada = []
                else:
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    puxar.append(comprarCarta(deck))
                    print ("Puxou a carta: ",puxar)
                    jogada = verSeTemCorOuNumero(puxar,cartaTopo)
                    if len(jogada)>0:
                        cartaTopo = puxar[0]
                        print("Jogou ",puxar)
                        verificaCarta(cartaTopo)
                    else:
                        baralhos[quemJoga].append(puxar[0])
                        print("pegou  ",baralhos[quemJoga])
                    puxar.clear()
                    jogada = []
            #rodada+=1
            jogada = []
                
            
        elif tipoCarta == "duas":
            puxarQuantas += 2
            if jaFoi == False:
                jogada = verSeTemDoisOuQuatro(baralhos[quemJoga])
                if len(jogada)>0:
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    jogar = random.choice(jogada)
                    cartaTopo = jogar
                    print("Jogou : ", jogar)
                    verificaCarta(cartaTopo)
                    baralhos[quemJoga].remove(jogar)
                    jogada = []
                    
            
                else:
                    print("Jogador ",jogadores[quemJoga]," puxou ",puxarQuantas,' cartas e passou a vez')
                    for n in range(puxarQuantas):    
                        baralhos[quemJoga].append(comprarCarta(deck))
                    puxarQuantas = 0
                    quemJoga = proximoJogador(quemJoga)
                    jaFoi = True
                    marcaRodada = rodada+2
                    jogada = []
                    
            else:
                jaFoi == False
                jogada = verSeTemCorOuNumero(baralhos[quemJoga],cartaTopo)
                if len(jogada)>0:
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    print("Opções para jogar: ",jogada)    
                    jogar = random.choice(jogada)
                    cartaTopo = jogar
                    print("Jogou : ", jogar)
                    verificaCarta(cartaTopo)
                    baralhos[quemJoga].remove(jogar)
                else:
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    puxar.append(comprarCarta(deck))
                    print ("Puxou a carta: ",puxar)
                    jogada = verSeTemCorOuNumero(puxar,cartaTopo)
                    if len(jogada)>0:
                        cartaTopo = puxar[0]
                        print("Jogou ",puxar)
                        verificaCarta(cartaTopo)
                    else:
                        baralhos[quemJoga].append(puxar[0])
                        print("pegou  ",baralhos[quemJoga])
                    puxar.clear()
                    jogada = []
            quemJoga = proximoJogador(quemJoga)
            #rodada+=1
            jogada = []
                
                
        elif tipoCarta == "quatro":
            puxarQuantas+=4
            if jaFoi == False:
                jogada = verSeTemQuatro(baralhos[quemJoga])
                print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                if len(jogada)>0:
                    jogar = random.choice(jogada)
                    cartaTopo = jogar
                    print("Jogou : ", jogar)
                    verificaCarta(cartaTopo)
                    baralhos[quemJoga].remove(jogar)

                else:
                    print("Jogador ",jogadores[quemJoga]," puxou ",puxarQuantas,' cartas')
                    for n in range(puxarQuantas):    
                        baralhos[quemJoga].append(comprarCarta(deck))
                    puxarQuantas = 0
                    jaFoi = True
                    marcaRodada = rodada+2
                    jogada = []
            
            else:
                jaFoi = False
                cor = random.choice(cores)
                print("Cor escolhida: ",cor)
                cartaTopo = cor + ' -'
                
                jogada = verSeTemCorOuNumero(baralhos[quemJoga],cartaTopo)
                if len(jogada)>0:
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    print("Opções para jogar: ",jogada)
                    print("Jogou : ", jogar)
                    jogar = random.choice(jogada)
                    cartaTopo = jogar
                    baralhos[quemJoga].remove(jogar)
                else:
                    print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                    puxar.append(comprarCarta(deck))
                    print ("Puxou a carta: ",puxar)
                    jogada = verSeTemCorOuNumero(puxar,cartaTopo)
                    if len(jogada)>0:
                        cartaTopo = puxar[0]
                        print("Jogou ",puxar)
                    else:
                        baralhos[quemJoga].append(puxar[0])
                        print("pegou  ",baralhos[quemJoga])
                    puxar.clear()
                    jogada = []
            quemJoga = proximoJogador(quemJoga)
            #rodada+=1
            jogada = []
        elif tipoCarta == "normal":
            jogada = verSeTemCorOuNumero(baralhos[quemJoga],cartaTopo)
            if len(jogada)>0:
                print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                print("Opções para jogar: ",jogada)    
                jogar = random.choice(jogada)
                cartaTopo = jogar
                print("Jogou : ", jogar)
                verificaCarta(cartaTopo)
                baralhos[quemJoga].remove(jogar)
                jogada = []
            else:
                print("Baralho do jogador ",jogadores[quemJoga]," : ",baralhos[quemJoga])
                puxar.append(comprarCarta(deck))
                print ("Puxou a carta: ",puxar)
                jogada = verSeTemCorOuNumero(puxar,cartaTopo)
                if len(jogada)>0:
                    cartaTopo = puxar[0]
                    print("Jogou ",puxar)
                    verificaCarta(cartaTopo)
                else:
                    baralhos[quemJoga].append(puxar[0])
                    print("pegou  ",baralhos[quemJoga])
                puxar.clear()
                rodada+=1
                jogada = []
            #rodada+=1
            jogada = []
            
        deck += descarte
        embaralhar(deck)
        rodada +=1
        
        if len(baralhos[quemJoga])==0:
            print("o jogador",jogadores[quemJoga], "Ganhou")
            venceu = True
            break
        elif len(baralhos[quemJoga])==1:
            print ("UNO!!")
        quemJoga = proximoJogador(quemJoga)
        #time.sleep(1)
        

if __name__ == "__main__":
    main()


