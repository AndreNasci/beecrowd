"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

days = int(input())

years = days // 365
months = days % 365 // 30
days -= (years * 365 + months * 30)

output = f'''{years} ano(s)
{months} mes(es)
{days} dia(s)'''

print(output)