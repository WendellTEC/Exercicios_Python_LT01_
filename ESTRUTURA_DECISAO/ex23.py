# 23. Receba 3 valores obrigatoriamente em ordem crescente e um 4o valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.

# Declarar
v1: int = 0
v2: int = 0
v3: int = 0
v4: int = 0

# Inicio
v1 = int(input("Informe o valor 1: "))
v2 = int(input("Informe o valor 2: "))

if v2 < v1:
    print("Error: O valor foge da ordem crescente")
    exit(0)

v3 = int(input("Informe o valor 3: "))

if v3 < v2:
    print("Error: O valor foge da ordem crescente")
    exit(0)
   
v4 = int(input("Informe o valor 4: "))

if v4 <= v1:
    print(v4, v1, v2, v3)
elif v4 > v1 and v4 <= v2:
    print(v1, v4, v2, v3)
elif v4 > v2 and v4 <= v3:
    print(v1, v2, v4, v3)
else:
    print(v1, v2, v3, v4)
# Fim