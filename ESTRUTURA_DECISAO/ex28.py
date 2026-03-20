# 28. Receba o preço atual e a média mensal de um produto. Calcule e mostre o novo preço sabendo que:
# Venda_Mensal Preço_Atual Preço_Novo
# < 500 < 30.00 + 10%
# >= 500 e < 1000 >= 30.00 e < 80.00 + 15%
# >= 1000 >= 80.00 - 5%
# Obs.: para outras condições, preço novo será igual ao preço atual.

# Declarar
preco_atual: float = 0.0
quantidade: int = 0
novo_preco: float = 0.0

# Inicio
preco_atual = float(input("Informe o valor atual do produto: R$"))
quantidade = int(input("Informe a quantidade de vendas mensais do produto: "))

if quantidade < 500 and preco_atual < 30.00:
    novo_preco = preco_atual * 1.1
elif quantidade >= 500 and quantidade < 1000 and preco_atual >= 30.00 and preco_atual < 80.00:
    novo_preco = preco_atual * 1.15
elif quantidade >= 1000 and preco_atual >= 80.00:
    novo_preco = preco_atual * 0.95
else:
    novo_preco = preco_atual

print("O novo preço é de: R$", round(novo_preco, 2))
