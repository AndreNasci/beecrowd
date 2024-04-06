"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

code_1, units_1, price_1 = input().split()
code_2, units_2, price_2 = input().split()

total = int(units_1) * float(price_1) + int(units_2) * float(price_2)

print(f"VALOR A PAGAR: R$ {total:.2f}")
