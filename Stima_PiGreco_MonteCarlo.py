import random

#Numero totale di punti da generare

total_punti = 100000
punti_cerchio = 0 #Contatore dei punti all'interno del cerchio

for _ in range(total_punti):
    # Genera le coordinate x e y causali all'interno del quadrato
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
    
    #Controlla se il punto è all'interno del cerchio
    if x**2 + y**2 <= 1:
        punti_cerchio += 1  
# Area del cerchio : pi * r^2 (dove r=1)
area_cerchio = punti_cerchio / total_punti
# Area del quadrato: lato^2 (dove lato=2)
area_quadrato = 4
#La proporzione tra l'area del cerchio e quella del quadrato è Pi/4
pi_greco_stimato = area_cerchio * 4

print("Stima di Pi Greco:", pi_greco_stimato) 
