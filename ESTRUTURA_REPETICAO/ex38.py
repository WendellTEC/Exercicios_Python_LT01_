# 38. Receba 100 números inteiros reais. Verifique e mostre o maior e o menor valor. Obs.: somente valores positivos.

# Declarar
n: float = 0.0
i: int = 0
maior: float = 0.0
menor: float = 0.0

# Inicio
while i < 100:
    n = float(input("Informe o valor: "))

    if n <= 0:
        print("SOMENTE VALORES POSITIVOS!")
    else:
        if i == 0:
            maior = n
            menor = n
        else:
            if n > maior:
               maior = n
            if n < menor:
                menor = n
        i += 1
               

print("Maior:", maior)
print("Menor:", menor)
# Fim