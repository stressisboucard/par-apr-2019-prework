Well_height = 125
D_advance = 30
N_retreat = 20
A_Distance = D_advance - N_retreat 
total_days = 0
position = 0 

print("je commence mon voyage ", total_days, " J'ai parcouru", position ,"sur le total ",Well_height)
while position<125:
    total_days +=1

    # 0 = 0 + 30
    # 30 = 30+30
    # 60= 60+30
    position = position + D_advance 


    #if <125:
     #   print("je tombe",i+1*d-r, "sur",w)
    #else: 
    #    print("je suis arrivée en", i+1,"days")
    print("Fin de journee ", total_days, " J'ai parcouru", position ,"sur le total ",Well_height)


print("J'ai terminé mon voyage journée ", total_days, " J'ai parcouru", position ,"sur le total ",Well_height)