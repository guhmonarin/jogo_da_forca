from time import sleep
from visual import visual
import os
import requests
import re
from lxml import html  
import os

def carregaPalavra():
    url = "http://www.palabrasaleatorias.com/palavras-aleatorias.php?fs=1"
    resposta = requests.get(url)
    elemento = html.fromstring(resposta.content)
    palavra = elemento.xpath('//div[@style="font-size:3em; color:#6200C5;"]/text()')
    palavra = palavra[0].strip()
    return palavra.lower()

def linhas():
    print('-'*50)

def Cabecalho():
    linhas()
    print(' '*18 + 'JOGO DA FORCA' + ' '*18)
    linhas()


def formarPalavra(palavra):
    return ['_' for letra in palavra]

def Menu():
    print('[1] - Chutar a letra!')
    print('[2] - Chutar a palavra')
    Opcao = int(input('Digite sua opção: '))
    return Opcao

def chutarLetra():
    letra = input('Digite a letra: ')
    return letra

def limparTela():
    os.system('cls')

def chutarPalavra():
    palavras = input('Digite a palavra: ')
    return palavras
def venceu():
    print("\nParabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

while True:
    Cabecalho()
    iniciar = input('Iniciar novo jogo? (S/N): ').lower()

    if iniciar == 'n':
        print('SAINDO DO JOGO')
        sleep(1)
        break

    tentativa = 7
    palavra_escolhida = carregaPalavra()
    letras_palavras = list(palavra_escolhida)
    letras_faltando = formarPalavra(letras_palavras)

    while True:
        
        limparTela()
        Cabecalho()
        print(visual.get(tentativa))
        print(str(letras_faltando)[1:-1])

        if '_' not in letras_faltando:
                venceu()
                break

        if tentativa == 0:
            print('GAME OVER')
            print(f'A palavra correta era {palavra_escolhida}')
            break

        opcao = Menu()
        
        if opcao == 1:
            letra = chutarLetra()
            index = 0
            if letra in palavra_escolhida:
                for letras in palavra_escolhida:
                    if letra == letras:
                        letras_faltando[index]=letra
                    index += 1
            else:
                tentativa -= 1

        elif opcao == 2:
            palavras = chutarPalavra()
            if palavras == palavra_escolhida:
                venceu()
                break
            else:
                print('VOCÊ ERROU A PALAVRA!')
                sleep(3)
                tentativa -= 1