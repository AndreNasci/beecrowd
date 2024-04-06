"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

value = int(input())
print(value)

banknotes = [100, 50, 20, 10, 5, 2, 1]
banknotes_quantity = []

for note in banknotes:
    banknotes_quantity.append(value // note)
    value %= note

for quantity, note in zip(banknotes_quantity, banknotes):
    print(f"{quantity} nota(s) de R$ {note},00")
