#Declaracao de Variaveis
ano_nasc: int = 0
ano_atual: int = 0
idade: int = 0

#Inicio
ano_nasc = int(input("Informe o ano do seu nascimento: "))
ano_atual = int(input("Informe o ano atual: "))
idade = ano_atual - ano_nasc
print(f"Voce tem {idade} anos")
print(f"Daqui a 17 anos voce vai ter {idade + 17} anos")
#Fim