A, B, C = map(float,input().split())

trianguloRetangulo = A * C / 2

circulo = 3.14159 * (C**2)

trapezio = ((A + B) * C) / 2

quadrado = B ** 2

retangulo = A * B

print("TRIANGULO: {:.3f}\nCIRCULO: {:.3f}\nTRAPEZIO: {:.3f}\nQUADRADO: {:.3f}\nRETANGULO: {:.3f}" .format(trianguloRetangulo, circulo, trapezio, quadrado,retangulo))
