# 24. Receba um valor inteiro. Verifique e mostre se é divisível por 2 e 3.

# Declarar
v: int = 0

# Inicio
v = int(input("Informe o valor: "))

if v % 2 == 0 and v % 3 == 0:
    print("É divisivel por 2 e por 3")
elif v % 2 == 0:
    print("É divisivel por 2")
elif v % 3 == 0:
    print("É divisivel por 3")
else:
    print("Não é divisivel por 2 nem por 3")
# Fim