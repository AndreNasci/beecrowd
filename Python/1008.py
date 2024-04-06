"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

employee_number = int(input())
worked_hours = int(input())
amount_per_hour = float(input())

salary = worked_hours * amount_per_hour

print("NUMBER =", employee_number)
print(f"SALARY = U$ {salary:.2f}")