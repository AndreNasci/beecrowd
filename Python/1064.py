"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

sum_avg = 0
pos_count = 0
for i in range(6):
    number = float(input())
    
    # Calculates the amount and the average of positive numbers
    if number > 0: 
        pos_count += 1 
        sum_avg += float(number)

print('{} valores positivos'.format(pos_count))
print(f'{(sum_avg / pos_count):.1f}')
