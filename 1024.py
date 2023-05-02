import math

casos = int(input())

for i in range(casos):
    mensagem = input()
    cifra = ""
    #1° passada
    for letra in mensagem:
        if letra.isupper() or letra.islower():
            novaLetra = ord(letra)+3
            novaLetra = chr(novaLetra)
        else:
            novaLetra = letra

        cifra = cifra + novaLetra
            
    #2° passada     
    cifra = (cifra[::-1])

    #3° passada
    metade = math.floor(len(cifra)//2)
    cifra = list(cifra)

    for j in range(metade,len(cifra)):
        codigoLetra = ord(cifra[j])-1
        cifra[j] = chr(codigoLetra)

    cifra = "".join(cifra)

    print(cifra)