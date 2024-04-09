"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

salary = float(input())

if salary <= 400:
    rate = 15
elif salary <= 800:
    rate = 12
elif salary <= 1200:
    rate = 10
elif salary <= 2000:
    rate = 7
else:
    rate = 4

reajuste = rate / 100.0 * salary

print(f"Novo salario: {reajuste + salary:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {rate} %")