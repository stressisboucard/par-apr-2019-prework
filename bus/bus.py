import math

#bus_stop = (in_, out) 

stops = [(5, 0), (5, 3), (3, 5), (5, 0)]

nombre_arret = len(stops)

nombre_de_passager = 0

liste_n_passagers = list()

#pour tuples 
for in_,out in stops: 
	nombre_de_passager += in_
	nombre_de_passager -= out
	print(in_,"personnes entrent", out,"personnes sortent")
	print("il y a",nombre_de_passager, "dans le bus" )
	# nombre_de_passager +=in_-out (equivalent)
	liste_n_passagers.append(nombre_de_passager)

max_n_passager = max(liste_n_passagers)

somme = sum(liste_n_passagers)
avg = somme / len(liste_n_passagers)
print("average = ",avg)

std = 0
for nombre in liste_n_passagers: #formule ecart type
	std += (nombre - avg)**2
std /= len(liste_n_passagers)
std = math.sqrt(std)
print("ecart type =",std)



