# 35. Receba 2 números inteiros, verifique qual o maior entre eles. Calcule e mostre o resultado da somatória dos números ímpares entre esses valores.

# Declarar
n1: int = 0
n2: int = 0
i: int = 0
soma: int = 0

# Inicio
n1 = int(input("Informe o valor 1: "))
n2 = int(input("Informe o valor 2: "))

if n1 == n2:
    print("Valores iguais!")
    exit(0)
elif n1 > n2:
    for i in range(n2 + 1, n1):
        if i % 2 == 1:
            soma += i
else:
    for i in range(n1 + 1, n2):
        if i % 2 == 1:
            soma += i

print(soma)
# Fim