"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

notes = [100, 50, 20, 10, 5, 2]
coins = [50, 25, 10, 5, 1]
coins_print = [1.0, 0.50, 0.25, 0.10, 0.05, 0.01]

notes_quantity = []
coins_quantity = []

value_coins = float(input())
value_notes = int(value_coins)

total = 0
for note in notes:
    notes_quantity.append(value_notes // note)
    value_notes %= note
    total += notes_quantity[-1] * note

coins_quantity.append(1) if value_notes else coins_quantity.append(0)

value_coins -= total + coins_quantity[-1]
value_coins = int(value_coins * 100)

for coin in coins:
    coins_quantity.append(value_coins // coin)
    value_coins %= coin

print("NOTAS:")
for quantity, note in zip(notes_quantity, notes):
    print(f"{quantity} nota(s) de R$ {note}.00")
print("MOEDAS:")
for quantity, coin in zip(coins_quantity, coins_print):
    print(f"{quantity} moeda(s) de R$ {coin:.2f}")