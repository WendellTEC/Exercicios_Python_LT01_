# 27. Receba o número de voltas, a extensão do circuito (em metros) e o tempo de duração (minutos). Calcule e mostre a velocidade média em km/h.

# Declarar
voltas: int = 0
metros: int = 0
minutos: int = 0
km: int = 0
horas: int = 0
velocidade_media: int = 0

# Inicio
voltas = int(input("Informe a quantidade de voltas: "))
metros = int(input("Informe a extensao em metros: "))
minutos = int(input("Informe a duração em minutos: "))

km = (metros / 1000) * voltas 
horas = minutos / 60
velocidade_media = km / horas

print("Velocidade media: ", velocidade_media)