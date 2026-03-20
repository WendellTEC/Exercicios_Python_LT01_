# 18. Receba 2 valores inteiros. Calcule e mostre o resultado da diferença do maior pelo menor valor.

# Declarar 
v1: int = 0
v2: int = 0
# Inicio
v1 = int(input("Informe o valor 1: "))
v2 = int(input("Informe o valor 2: "))

if v1 > v2: 
    print(v1 - v2)
elif v1 < v2:
    print(v2 - v1)
else:
    print("Valores iguais diferença = 0")
# Fim