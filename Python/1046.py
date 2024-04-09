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

inicio, fim = converte_lista_int(input().split())

if inicio >= fim:
    duracao = fim + 24 - inicio
else:
    duracao = fim - inicio

print(f"O JOGO DUROU {duracao} HORA(S)")