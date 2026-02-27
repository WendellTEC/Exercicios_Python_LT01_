#Declaracao de Variaveis
tempo_percurso: int = 0
velocidade_media: int = 0
kilometragem_total: int = 0
quantidade_litros: int = 0

#Inicio
tempo_percurso = int(input("Informe o tempo do percurso: "))
velocidade_media = int(input("Informe a velocidade media: "))
kilometragem_total = tempo_percurso * velocidade_media
quantidade_litros = kilometragem_total / 12
print(f"O total de litros gasto na viagem e de: {round(quantidade_litros)}l") 
#Fim