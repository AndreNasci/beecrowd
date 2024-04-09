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

lista_input = converte_lista_int(input().split())

for i in sorted(lista_input):
    print(i)

print()

for i in lista_input:
    print(i)