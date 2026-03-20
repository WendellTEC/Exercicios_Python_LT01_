# 33. Receba um número. Calcule e mostre a série 1 + 1/2 + 1/3 + ... + 1/N.

# Declarar
i: int = 0
n: int = 0
soma: float = 0.0

# Inicio
n = int(input("Informe o valor de N: "))

for i in range (1, n + 1):
    soma += 1 / i

print(soma)
# Fim