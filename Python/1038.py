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



x, y = converte_lista_int(input().split())

price_dict = {1: 4.00, 2: 4.50, 3: 5.00, 4: 2.00, 5: 1.50}

print(f"Total: R$ {(price_dict[x] * y):.2f}")


