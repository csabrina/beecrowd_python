hI, mI, hF, mF = map(int,input().split())

entrada = [int(i) for i in input().split()]

hI = entrada[0]
mI = entrada[1]
hF = entrada[2]
mF = entrada[3]


hTotal= hF - hI
mTotal = mF - mI

if (hTotal < 0):
    hTotal += 24

if (mTotal < 0):
    mTotal += 60
    hTotal -= 1

if (hI == 0 and mI == 0):
    print("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
else:
    print("O JOGO DUROU {} HORA(S) E {} MINUTOS" .format(hTotal, mTotal))'

#----------------------------------------------------------------------------------------------

[hI, mI, hF, mF] = input().split()
hI = int(hI)
mI = int(mI)
hF = int(hF)
mF = int(mF)

mI += hI * 60
mF += hF * 60

duracao = mF - mI

if (duracao <= 0):
    duracao += (24 * 60)

hora = int(duracao / 60)
min = duracao % 60

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)" .format(hora,min))