#Declaracao de Variaveis
celsius: float = 0.0
fahrenheit: float = 0.0

#Inicio
celsius = float(input("Informe a temperatura em Celsius: "))
fahrenheit = (9 * celsius + 160) / 5
print(f"A temperatura convertida para Fahrenheit é: {fahrenheit}")
#Fim