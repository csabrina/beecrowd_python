nota = int(input())

if 0 <= nota <= 100:
    if nota == 0:
        print("E")
    elif nota < 36:
        print("D")
    elif nota < 61:
        print("C")
    elif nota < 86:
        print("B")
    else:
        print("A")
else:
    print("Digite uma nota válida (entre 0 e 100)")