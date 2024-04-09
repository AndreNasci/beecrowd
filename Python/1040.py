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

n1, n2, n3, n4 = converte_lista_float(input().split())

media_ponderada = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

print(f"Media: {media_ponderada:.1f}")

if media_ponderada >= 7:
    print("Aluno aprovado.")
elif media_ponderada >= 5:
    print("Aluno em exame.")
    nota_exame = float(input())
    print(f"Nota do exame: {nota_exame:.1f}")
    nova_media = (nota_exame + media_ponderada) / 2
    print("Aluno aprovado.") if nova_media >= 5 else print("Aluno reprovado.")
    print(f"Media final: {nova_media:.1f}") 
else:
    print("Aluno reprovado.")