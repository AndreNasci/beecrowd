"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

number = float(input())

if number > 100 or number < 0:
    print("Fora de intervalo")
elif number <= 25:
    print("Intervalo [0,25]")
elif number <= 50:
    print("Intervalo (25,50]")
elif number <= 75:
    print("Intervalo (50,75]")
else:
    print("Intervalo (75,100]")
    
