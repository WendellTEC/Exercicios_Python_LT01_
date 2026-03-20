# 32. Receba um número inteiro. Calcule e mostre o seu fatorial.

# Declarar
i: int = 0
n: int = 0
f: int = 1

# Inicio
n = int(input("Informe o valor a ser fatorado: "))

for i in range(1, n + 1):
    f *= i

print(f)
# Fim