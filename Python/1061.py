"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

dia_inicio = input()
dia_inicio = int(dia_inicio[4:])

h1, m1, s1 = list(map(int, input().split(sep=' : ')))


dia_fim = input()
dia_fim = int(dia_fim[4:])

h2, m2, s2 = list(map(int, input().split(sep=' : ')))

segundos = 0

if dia_inicio == dia_fim:

    # Calcular segundos do momento de fim
    seg_fim = h2 * 3600 + m2 * 60 + s2
    
    # Calcular segundos momento de inicio
    seg_inicio = h1 * 3600 + m1 * 60 + s1

    # Diferença entre dois momentos
    segundos = seg_fim - seg_inicio

else:
    # Calcular segundos do dia fim
    segundos += h2 * 3600 + m2 * 60 + s2

    # Calcular segundos do dia inicio
    segundos += (24 - h1) * 3600 + (60 - m1) * 60 + (60 - s1)
    if s1 != 0 and m1 != 0: segundos -= 3600
    if s1 != 0: segundos -= 60

    # Acrescentar segundos entre os dias
    segundos += (dia_fim - dia_inicio - 1) * 24 * 3600

# Converter segundos em dias, horas, minutos e segundos
minutos = segundos // 60
segundos = segundos % 60

horas = minutos // 60 
minutos = minutos % 60

dias = horas // 24
horas = horas % 24

# Exibir informações
print(f'{dias} dia(s)')
print(f'{horas} hora(s)')
print(f'{minutos} minuto(s)')
print(f'{segundos} segundo(s)')

