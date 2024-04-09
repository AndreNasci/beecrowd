"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

def converte_lista_int(lista_str):
    lista_int = []
    for numero in lista_str:
        lista_int.append(int(numero))
    return lista_int

def calcula_duracao_minutos(inicio, fim):
    if fim < inicio:
        return 60 - inicio + fim 
    else: 
        return fim - inicio


h_inicio, min_inicio, h_fim, min_fim = converte_lista_int(input().split())

if h_inicio >= h_fim and min_fim <= min_inicio:
    h_duracao = h_fim + 24 - h_inicio
else:

    h_duracao = h_fim - h_inicio

min_duracao = calcula_duracao_minutos(min_inicio, min_fim)
if min_fim < min_inicio:
    h_duracao -= 1

print(f"O JOGO DUROU {h_duracao} HORA(S) E {min_duracao} MINUTO(S)")
