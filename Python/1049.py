"""
André Nascimento
GitHub: github.com/AndreNasci
Linkedin: linkedin.com/in/andre-nasci/
"""
word_1 = input()
word_2 = input()
word_3 = input()



if word_1 == 'vertebrado':
    if word_2 == 'ave':
        if word_3 == 'carnivoro':
            animal = 'aguia'
        else:
            # onívoro
            animal = 'pomba'
    else:
        # mamífero
        if word_3 == 'onivoro':
            animal = 'homem'
        else:
            # herbívoro
            animal = 'vaca'
else:
    # invertebrado
    if word_2 == 'inseto':
        if word_3 == 'hematofago':
            animal = 'pulga'
        else:
            # herbívoro
            animal = 'lagarta'
    else:
        # anelideo
        if word_3 == 'hematofago':
            animal = 'sanguessuga'
        else:
            # onivoro
            animal = 'minhoca'

print(animal)