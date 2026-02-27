#Declaracao de Variaveis
horas_t: int = 0
valor_h: float = 0
percentual_desconto: int = 0
numero_descendentes: int = 0
desconto: float = 0.0
salario: float = 0
salario_liquido: float = 0

#Inicio
horas_t = int(input("Informe a quantidade de horas trabalhadas: "))
valor_h = float(input("Informe o valor a receber por hora: "))
percentual_desconto = int(input("Informe o percentual de desconto: "))
numero_descendentes = int(input("Informe a quantidade de descendentes: "))
desconto = (percentual_desconto / 100)
salario = horas_t * valor_h
salario_liquido = (salario - (salario * desconto)) + (100 * numero_descendentes) 
print(f"O salario liquido é: R${salario_liquido}")
#Fim