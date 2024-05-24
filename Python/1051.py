"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

salario = float(input())

taxes = 0.
if salario > 4500.0:
    taxes += (salario - 4500) * 0.28
    salario = 4500

if salario > 3000.0:
    taxes += (salario - 3000.0) * 0.18
    salario = 3000

if salario > 2000.0:
    taxes += (salario - 2000.0) * 0.08
    salario = 2000

if taxes:
    print(f'R$ {taxes:.2f}')
else:
    print('Isento')

