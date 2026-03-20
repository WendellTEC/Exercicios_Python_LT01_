#Declaracao de Variaveis
deposito: float = 0.0
renda: float = 0.0

#Inicio
deposito = float(input("Informe o valor do deposito: R$"))
renda = deposito * 1.013
print(f"Apos um mes de aplicacao o valor é de: R${round(renda, 2)}")
#Fim