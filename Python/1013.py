"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

def maior_ab(a, b):
    return int((a + b + abs(a - b)) / 2)

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

maior = maior_ab(A, B)
maior = maior_ab(maior, C)

print(f"{maior} eh o maior")
