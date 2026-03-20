#Declaracao de Variaveis
salario: float = 0.0
salario_novo: float = 0.0

#Inicio
salario = float(input("Informe o salario atual do funcionario: R$"))
salario_novo = salario * 1.15
print(f"O novo salario é de: R${round(salario_novo, 2)}")
#FIM
