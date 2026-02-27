#Declaracao de variaveis
x: int = 0
y: int = 0
valor_x: int = 0
valor_y: int = 0

#Inicio
x = int(input("Informe o valor de x: "))
y = int(input("Informe o valor de y: "))
valor_x = x
valor_y = y 
x = valor_y
y = valor_x
print(f"X: {x}")
print(f"Y: {y}")
#Fim