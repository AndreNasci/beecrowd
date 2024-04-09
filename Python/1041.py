"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

def converte_lista_float(lista_str):
    lista_float = []
    for numero in lista_str:
        lista_float.append(float(numero))
    return lista_float

x, y = converte_lista_float(input().split())

if x == 0:
    if y == 0:
        print("Origem")
    else:
        print("Eixo Y")
elif y == 0:
    print("Eixo X")
else:
    if x > 0:
        if y > 0:
            print("Q1")
        else:
            print("Q4")
    else:
        if y > 0:
            print("Q2")
        else:
            print("Q3")
