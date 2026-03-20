# 34. Receba um número. Calcule e mostre os resultados da tabuada desse número.

# Declarar
n: int = 0
i: int = 0

# Inicio
n = int(input("Informe o valor de N: "))

for i in range (1, 11):
    print(f"{n} x {i} = {n*i}")
# Fim