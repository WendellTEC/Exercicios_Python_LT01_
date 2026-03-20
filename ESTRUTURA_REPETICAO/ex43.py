# 43. Calcule e mostre quantos anos serão necessários para que Ana seja maior que Maria sabendo que Ana tem 1,10 m e cresce 3 cm ao ano e Maria tem 1,5 m e cresce 2 cm ao ano.

# Declarar
ana: int = 110
maria: int = 150
anos: int = 0

# Inicio
while (ana <= maria):
    ana += 3
    maria += 2
    anos += 1

print(anos, "Anos")
# Fim