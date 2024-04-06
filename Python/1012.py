"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

A, B, C = input().split()
A = float(A)
B = float(B)
C = float(C)

pi = 3.14159 

print(f"TRIANGULO: {(A * C / 2):.3f}")
print(f"CIRCULO: {(pi * C ** 2):.3f}")
print(f"TRAPEZIO: {((A + B) * C / 2):.3f}")
print(f"QUADRADO: {(B ** 2):.3f}")
print(f"RETANGULO: {(A * B):.3f}")
