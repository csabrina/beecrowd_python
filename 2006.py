tipo = int(input())
count = 0

if 1<=tipo<=4:
    resposta = map(int,input().split())
    for i in resposta:
        if i == tipo:
            count += 1
    print(count)
else:
    print("Digite um tipo de chá válido")