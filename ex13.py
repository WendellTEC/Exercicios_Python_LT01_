#Declaracao de Variaveis
quantidade_kg: float = 0.0
quantidade_g: float = 0.0
dias: int = 0

#Inicio
quantidade_kg = float(input("Informe a quantidade de um alimento em kilos: "))
quantidade_g = quantidade_kg * 1000
dias = quantidade_g / 50
print(f"O alimento durara por {round(dias)} dias")
#Fim