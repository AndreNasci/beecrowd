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


A, B, C = converte_lista_float(input().split())


delta = B ** 2 - 4 * A * C

if A == 0 or delta < 0:
    print("Impossivel calcular")
else:
    if delta == 0:
        r1 = (0 - B) / (2.0 * A) 
        r2 = r1
    else:
        delta_sqrt = delta ** 0.5
        r1 = (- B + delta_sqrt) / (2.0 * A)
        r2 = (- B - delta_sqrt) / (2.0 * A)

    print(f"R1 = {r1:.5f}")
    print(f"R2 = {r2:.5f}")