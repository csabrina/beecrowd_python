pressaoDesejada = int(input())
pressaoAtual = int(input())

if 1<=pressaoDesejada<=40 and 1<=pressaoAtual<=40:
    diferenca = pressaoDesejada - pressaoAtual
    print(diferenca)
else:
    print("Digite valores válidos (entre 1 e 40)")