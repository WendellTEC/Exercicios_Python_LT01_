# 41. Mostre todas as possibilidades de 2 dados de forma que a soma tenha como resultado 7.

# Declarar
dado1: int = 0
dado2: int = 0
i: int = 0

# Inicio
for dado1 in range (1, 7):
    for dado2 in range (1, 7):
        if dado1 + dado2 == 7:
            print(dado1, "+", dado2)
# Fim