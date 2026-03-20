import math

#Declaracao de Variaveis
a: int = 0
b: int = 0
c: int = 0
delta: int = 0
raiz1: int = 0
raiz2: int = 0 

#Inicio
a = int(input("Informe o valor do coeficiente A: "))
b = int(input("Informe o valor do coeficiente B: "))
c = int(input("Informe o valor do coeficiente C: "))
delta = (b**2) - (4 * a * c)
raiz1 = (-(b) + math.sqrt(delta)) / 2 * a  
raiz2 = (-(b) - math.sqrt(delta)) / 2 * a  
print(f"A raiz 1 é: {raiz1}")
print(f"A raiz 2 é: {raiz2}")
#Fim