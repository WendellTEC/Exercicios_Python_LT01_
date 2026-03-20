# 45. Calcule e mostre a série 1 – 2/4 + 3/9 – 4/16 + 5/25 - ... + 15/225

# Declarar
termo: int = 0
i: int = 0
soma: int = 0

# Inicio
for i in range(1, 16):
    termo= i / (i * i)

    if i % 2 == 0:
        soma -= termo
    else:
        soma += termo

print(soma)
# Fim