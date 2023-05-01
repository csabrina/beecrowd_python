
salario = float(input())
imposto = 0

if 0 <= salario <= 2000:
    print("Isento")
elif 2000 < salario <= 3000:
    imposto = (salario - 2000) * 0.08
    print("R$ {:.2f}" .format(imposto))
elif 3000 < salario <= 4500:
    imposto = ((salario - 3000)  * 0.18) + 80
    print("R$ {:.2f}" .format(imposto))
else:
    imposto = ((salario - 4500) * 0.28) + 350
    print("R$ {:.2f}" .format(imposto))


