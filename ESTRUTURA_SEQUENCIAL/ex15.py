import math

#Declaracao de Variaveis
cateto_oposto: float = 0.0
cateto_adjacente: float = 0.0
hipotenusa: float = 0.0

#Inicio
cateto_oposto = float(input("Informe o valor do cateto Oposto: "))
cateto_adjacente = float(input("Informe o valor do cateto adjacente:"))
hipotenusa = math.sqrt((cateto_oposto**2) + (cateto_adjacente**2))
print(f"O valor da hipotenusa é: {round(hipotenusa, 2)}")
#Fim