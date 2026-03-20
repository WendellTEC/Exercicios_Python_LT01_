# 40. Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.

# Declarar
n1: int = 0
n2: int = 0
i: int = 0
j: int = 0 
primo: bool = False

# Inicio
n1 = int(input("Informe o valor 1:"))
n2 = int(input("Informe o valor 2:"))

if n1 > n2:
    n1, n2 = n2, n1

for i in range(n1, n2 + 1):
    if i > 1:
        primo = True

        for j in range(2, int(i ** 0.5)+ 1):
            if i % j == 0:
                primo = False
                break
        if primo:
            print(i)
# Fim            