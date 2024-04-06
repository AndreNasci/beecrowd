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

x1, y1 = input().split()
x2, y2 = input().split()

x1, y1, x2, y2 = converte_lista_float([x1, y1, x2, y2])

distance = ((x2 - x1) ** 2  + (y2 - y1) ** 2) ** 0.5

print(f"{distance:.4f}")