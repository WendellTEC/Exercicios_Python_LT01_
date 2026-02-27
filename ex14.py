#Declaracao de Variaveis
ang1: int = 0
ang2: int = 0
ang3: int = 0

#Inicio
ang1 = int(input("Informe o valor do angulo 1: "))
ang2 = int(input("Informe o valor do angulo 2: "))
ang3 = 180 - (ang1 + ang2)
print(f"O terceiro angulo tem o valor de: {ang3}°") 
#Fim