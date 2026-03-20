# 36. Receba um número N. Calcule e mostre a série 1 + 1/1! + 1/2! + ... + 1/N!

# Declarar
n: int = 0
i: int = 0
soma: float = 1.0
fat: int = 1

# Inicio
n = int(input("Informe o valor de N: "))

for i in range (1, n + 1):
    fat *= i
    soma += 1/fat

print(soma)
# Fim