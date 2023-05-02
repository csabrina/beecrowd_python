salario = float(input())

if 400 >= salario >= 0:
    percentual= "15 %"
    reajuste = salario * 0.15
    salarioFinal = salario + reajuste

elif 800 >= salario > 400:
    percentual= "12 %"
    reajuste = salario * 0.12
    salarioFinal = salario + reajuste

elif 1200 >= salario > 800:
    percentual = "10 %"
    reajuste = salario * 0.10
    salarioFinal = salario + reajuste

elif 2000 >= salario > 1200:
    percentual = "7 %"
    reajuste = salario * 0.07
    salarioFinal = salario + reajuste

elif salario > 2000:
    percentual = "4 %"
    reajuste = salario * 0.04
    salarioFinal = salario + reajuste

print(f"Novo salario: {salarioFinal:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual}")




