# 44. Receba o número da base e do expoente. Calcule e mostre o valor da potência.

# Declarar 
base: int = 0
expoente: int = 0
valor: int = 0
i: int = 0

# Inicio
base = int(input("Informe o valor da base: "))
expoente = int(input("Informe o valor do expoente: "))
valor = base

for i in range (expoente - 1):
    valor *= base
print(valor)
# Fim