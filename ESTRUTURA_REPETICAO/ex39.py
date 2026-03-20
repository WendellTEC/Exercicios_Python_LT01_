# 39. Calcule a quantidade de grãos contidos em um tabuleiro de xadrez onde:
# Casa: 1 2 3 4 ... 64
# Qdte: 1 2 4 8 ... N

# Declarar
casa: int = 0
qdte: int = 1
total: int = 0

# Inicio
for casa in range(64):
    total += qdte
    qdte *= 2
print(total)
# Fim