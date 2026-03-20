#20. Receba 3 coeficientes A, B, e C de uma equação do 2o grau da fórmula AX2+BX+C=0. Verifique e mostre a existência de raízes reais e se caso exista, calcule e mostre.

import math

# Declarar
a: int = 0
b: int = 0
c: int = 0
delta: int = 0
x1: int = 0
x2: int = 0

# Inicio
a = int(input("Informe o valor do coeficiente A: "))
b = int(input("Informe o valor do coeficiente B: "))
c = int(input("Informe o valor do coeficiente C: "))
delta = (b**2) - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a) 
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("A equacao possui duas raizes reais:")
    print(f"x1 = {round(x1)}, x2 = {round(x2)}")
elif delta == 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A equacao possui raiz real dupla:")
    print(f"x1 e x2 = {round(x1)}")
else:
    print("A equacao nao possui raizes!")
# Fim