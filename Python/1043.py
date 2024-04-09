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

a, b, c = converte_lista_float(input().split())

if ((a + b) > c and (a + c) > b and (b + c) > a) and (abs(a - b) < c and abs(a - c) < b and abs(b - c) < a):
    print(f"Perimetro = {(a + b + c):.1f}")
else:
    print(f"Area = {(a + b) * c / 2:.1f}")