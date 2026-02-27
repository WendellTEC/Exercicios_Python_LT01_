#Declaracao de variaveis 
comprimento: float = 0.0
largura: float = 0.0
altura: float = 0.0
volume: float = 0.0

#Inicio
comprimento = float(input("Informe o valor do comprimento: "))
largura = float(input("Informe o valor da largura: "))
altura = float(input("Informe o valor da altura: "))
volume = comprimento * largura * altura
print(f"O volume do paralelepipedo é de: {volume}")
#Fim