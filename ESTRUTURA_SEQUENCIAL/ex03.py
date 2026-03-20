#Declaracao de Variaveis
base: float = 0.0
altura: float = 0.0
area: float = 0.0

#Inicio
base = float(input("Informe o valor da base do triangulo: "))
altura = float(input("Informe o valor da altura do triangulo: "))
area = (base * altura) / 2
print(f"A area do triangulo é: {area}")
#FIM
