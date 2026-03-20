# 42. Calcule e mostre a série 1 + 2/3 + 3/5 + ... + 50/99

# Declarar
d: int = 1
i: int = 0
soma: int = 0

# Inicio
for i in range(1, 51):
    soma += i / d
    d += 2
print(soma)
# Fim