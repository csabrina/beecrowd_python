A, B, C, D = map(float,input().split())


media = (A*2 + B*3 + C*4 + D)/10
print("Media: {:.1f}".format(media))

if media >= 7:
    print("Aluno aprovado.")

elif media < 5:
    print("Aluno reprovado.")

else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: {:.1f}" .format(exame))
    media = (media + exame)/2

    if media >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print("Media final: {:.1f}" .format(media))