gandalf = [10,11,13,30,22,11,10,33,22,22]
saruman = [23,66,12,43,12,10,44,23,12,17]

score_g = 0
score_s = 0


for i in range(len(gandalf)): # for i in [0,1,2,3,4,5,6,7,8,9]:

	if gandalf[i] > saruman[i]: 
		score_g += 1 # score_g = score_g + 1 
		print('Gandalf remporte la manche.')

	elif saruman[i] > gandalf[i]: 
		score_s += 1
		print('Saruman remporte la manche.')

	else:
		print('Egalité pour cette manche.')
	#	score_g += 1
	# score_s += 1


if score_g > score_s: 
	print('Gandalf gagne.')

elif score_s > score_g: 
	print('Saruman gagne.')

else: 
	print('Egalité')


POWER = {
    'Fireball': 50, 
    'Lightning bolt': 40, 
    'Magic arrow': 10, 
    'Black Tentacles': 25, 
    'Contagion': 45
}

n_gandalf = 0
n_saruman = 0

gandalf = ['Fireball', 'Lightning bolt', 'Lightning bolt', 'Magic arrow', 'Fireball', 
           'Magic arrow', 'Lightning bolt', 'Fireball', 'Magic arrow', 'Fireball']
saruman = ['Contagion', 'Contagion', 'Black Tentacles', 'Fireball', 'Black Tentacles', 
           'Lightning bolt', 'Magic arrow', 'Contagion', 'Magic arrow', 'Magic arrow']

for i in range(len(gandalf)):
	if POWER [gandalf [i]] > POWER [saruman[i]]:
	 	n_gandalf += 1
	 	n_saruman = 0

	elif POWER[gandalf[i]]< POWER [saruman[i]]: 
	 	n_saruman += 1
	 	n_gandalf = 0 

	if n_gandalf == 3:
		print("gandalf remporte la manche")
	if n_saruman == 3: 
		print("saruman remporte la manche")

import math

liste = [10,11,13,30,22,11,10,33,22,22]

somme = 0

for i in range(len(liste)):
	somme += liste[i]

somme = 0
for nombre in liste:
	somme += nombre

somme = sum(liste)


avg = somme / len(liste)


std = 0
for nombre in liste:
	std += (nombre - avg)**2
std /= len(liste)
std = math.sqrt(std)
