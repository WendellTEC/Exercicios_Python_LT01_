# 19. Receba 2 valores reais. Calcule e mostre o maior deles.

# Declarar
v1 : float = 0.0
v2 : float = 0.0

# Inicio
v1 = float(input("Informe o valor 1: "))
v2 = float(input("Informe o valor 2:"))
if v1 > v2:
    print(v1, "é o maior!")
elif v1 < v2:
    print(v2, "é o maior!")
else:
    print("Valores iguais!")
# Fim