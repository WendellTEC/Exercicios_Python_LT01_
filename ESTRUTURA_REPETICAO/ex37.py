# 37. Receba um número inteiro. Calcule e mostre a série de Fibonacci até o seu N’nésimo termo.

# Declarar 
n: int = 0
a: int = 0
b: int = 1
i: int = 0
proximo: int = 0

# Inicio
n = int(input("Infome o valor de N: "))

for i in range (0, n + 1):
    print(a)
    proximo = a + b
    a = b
    b = proximo
# Fim