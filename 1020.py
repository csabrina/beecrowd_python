idadeEmDias = int(input())
dias = 0

anos = idadeEmDias // 365
idadeEmDias = idadeEmDias % 365

meses = idadeEmDias // 30
dias = idadeEmDias % 30

print("{} ano(s)\n{} mes(es)\n{} dia(s)" .format(anos, meses, dias))