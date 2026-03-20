# 22. Receba 2 valores inteiros e diferentes. Mostre seus valores em ordem crescente.

# Declarar
v1: int = 0
v2: int = 0

# Inicio
v1 = int(input("Informe o valor 1: "))
v2 = int(input("Informe o valor 2, precisa ser diferento do valor 1: "))
if v1 == v2:
    print("Error: VALORES IGUAIS!")
elif v1 < v2:
    print(v1, v2)
else:
    print(v2, v1)
# Fim