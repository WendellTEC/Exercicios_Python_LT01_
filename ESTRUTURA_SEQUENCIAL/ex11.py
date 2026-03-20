#Declaracao de Variaveis
raio: float = 0.0
comprimento: float = 0.0

#Inicio
raio = float(input("Informe o valor do raio da circunferencia: "))
comprimento = 2 * 3.14 * raio
print(f"O comprimento da circunferencia é de: {round(comprimento, 2)}")
#Fim