# 29. Receba o tipo de investimento (1 = poupança e 2 = renda fixa) e o valor do investimento. Calcule e mostre o valor corrigido em 30 dias sabendo que a poupança = 3% e a renda fixa = 5%. Demais tipos não serão considerados.

# Declarar
tipo_investimento: int = 0
valor_investimento: float = 0.0
valor_corrigido: float = 0.0
poupanca: float = 1.03
renda_fixa: float = 1.05

# Inicio
print("Informe o tipo de investimento!")
print("1 - Poupança")
print("2 - Renda fixa")
tipo_investimento = int(input("Escolha: "))

if tipo_investimento < 1 or tipo_investimento > 2:
    print("Error: Tipo invalido!")
    exit(0)

valor_investimento = float(input("Informe o valor a ser investido: R$"))

if valor_investimento <= 0.0:
    print("Error: Operação invalida!")
    exit(0)

if tipo_investimento == 1:
    valor_corrigido = valor_investimento * poupanca
else: 
    valor_corrigido = valor_investimento * renda_fixa

print("Valor apos 30 dias: R$", valor_corrigido)