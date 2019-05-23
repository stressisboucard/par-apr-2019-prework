Well_height = 125
D_advance = 0
N_retreat = 20
A_Distance = D_advance - N_retreat 
total_days = 0
position = 0 
tableau = [30, 21, 33, 77, 44, 45, 23, 45, 12, 34, 55]

print("je commence mon voyage ", total_days, " J'ai parcouru", position ,"sur le total ",Well_height)
while position<125:
    D_advance = tableau[total_days]
    total_days +=1

    position = position + D_advance 

    print("Fin de journee ", total_days, " J'ai parcouru", position ,"sur le total ",Well_height)


print("J'ai terminé mon voyage journée ", total_days, " J'ai parcouru", position ,"sur le total ",Well_height)