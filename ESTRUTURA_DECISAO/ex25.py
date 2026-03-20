# 25. Receba a hora de início e de final de um jogo (HH,MM), calcular o tempo do jogo em horas e minutos, sabendo que o tempo máximo é menor que 24 horas e pode começar num dia e terminar noutro.

# Declarar
hh_inicio: int = 0
hh_fim: int = 0
mm_inicio: int = 0
mm_fim: int = 0
inicio: int = 0
fim: int = 0
duracao: int = 0

# Inicio
# Entrada de dados e tratamento de erros
hh_inicio = int(input("Informe o horario de inicio do jogo (HH): "))
if hh_inicio < 0 or hh_inicio > 23:
    print("Error: Valor invalido!")
    exit(0)

mm_inicio = int(input("Informe o horario de inicio do jogo (MM): "))
if mm_inicio < 0 or mm_inicio > 59:
    print("Error: Valor invalido!")
    exit(0)

hh_fim = int(input("Informe o horario de fim do jogo (HH): "))
if hh_fim < 0 or hh_fim > 23:
    print("Error: Valor invalido!")
    exit(0)

mm_fim = int(input("Informe o horario de fim do jogo (MM): "))
if mm_fim < 0 or mm_fim > 59:
    print("Error: Valor invalido!")
    exit(0)

inicio = hh_inicio * 60 + mm_inicio
fim = hh_fim * 60 + mm_fim

if fim < inicio:
    fim += 24 * 60

duracao = fim - inicio

print(f"O jogo durou {duracao // 60} Horas e {duracao % 60} Minutos")
# Fim