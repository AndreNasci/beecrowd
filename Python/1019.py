"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""

seconds = int(input())

minutes = seconds // 60
seconds = seconds % 60

hours = minutes // 60
minutes = minutes % 60

print(f"{hours}:{minutes}:{seconds}")