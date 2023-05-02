nomeDoVendedor = input()
salarioFixo = float(input())
vendasEfetuadas = float(input())

total = (((vendasEfetuadas * 15) / 100) + salarioFixo)

print("TOTAL = R$ {:.2f}" .format(total))