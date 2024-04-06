"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

seller_name = input()
fixed_salary = float(input())
month_sales = float(input())

final_salary = fixed_salary + month_sales * 0.15

print(f"TOTAL = R$ {final_salary:.2f}")