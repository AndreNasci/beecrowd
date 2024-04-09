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

a, b = converte_lista_int(input().split())

if a % b == 0 or b % a == 0:
    print("Sao Multiplos")
else:
    print("Nao sao Multiplos")