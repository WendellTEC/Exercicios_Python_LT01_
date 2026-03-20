# 21. Receba 4 notas bimestrais de um aluno. Calcule e mostre a média aritmética. Mostre a
# mensagem de acordo com a média:
# a. Se a média for >= 6,0 exibir “APROVADO”;
# b. Se a média for >= 3,0 ou < 6,0 exibir “EXAME”;
# c. Se a média for < 3,0 exibir “RETIDO”.

# Declarar
n1: float = 0.0
n2: float = 0.0
n3: float = 0.0
n4: float = 0.0
m: float = 0.0

# Inicio
n1 = float(input("Informe a nota bimestral 1: "))
n2 = float(input("Informe a nota bimestral 2: "))
n3 = float(input("Informe a nota bimestral 3: "))
n4 = float(input("Informe a nota bimestral 4: "))

m = (n1 + n2 + n3 + n4) / 4

if m >= 6.0:
    print("APROVADO")
elif m >= 3.0 and m < 6.0:
    print("EXAME")
else:
    print("RETIDO")
# Fim