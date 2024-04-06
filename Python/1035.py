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


A, B, C, D = converte_lista_int(input().split())

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and not(A % 2):
    print("Valores aceitos")
else:
    print("Valores nao aceitos")