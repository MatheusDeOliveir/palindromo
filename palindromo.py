#Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e 
#OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados.
# A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
# Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
import os
import time

def verifica_se_e_palindromo(entrada):
    entrada = entrada.lower()
    letras = list()
    for letra in entrada:
        letras.append(letra)
    for item in letras:
        if item == ' ':
            letras.remove(item)
    print (letras)
    if letras[::1] == letras[::-1]:
        return True
    else:
        return False

while True:
    entrada = input ("Digite uma palavra ou frase e vou verificar se é um palíndromo ou não: ")
    if verifica_se_e_palindromo(entrada):
        print ("É um palíndromo!")
        time.sleep(3)
        os.system('cls')
        continue
    else:
        print ("Não é um palíndromo.")
        time.sleep(3)
        os.system('cls')
        continue
    
    
    
    
    