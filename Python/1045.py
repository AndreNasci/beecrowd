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

a, b, c = sorted(converte_lista_float(input().split()), reverse=True)

if a >= (b + c): 
    print("NAO FORMA TRIANGULO")
else:        
    if a ** 2 == b ** 2 + c ** 2: 
        print("TRIANGULO RETANGULO")
    if a ** 2 > b ** 2 + c ** 2: 
        print("TRIANGULO OBTUSANGULO")
    if a ** 2 < b ** 2 + c ** 2: 
        print("TRIANGULO ACUTANGULO")
    if a == b and a == c: 
        print("TRIANGULO EQUILATERO")
    elif a == b or b == c or a == c:
        print("TRIANGULO ISOSCELES")