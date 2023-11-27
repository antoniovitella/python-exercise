import random

numero_da_indovinare = random.randint(1, 100)
tentativi = 0

while True:
    tentativo = int(input("Indovina il numero (da 1 a 100): "))
    tentativi += 1
    
    if tentativo < numero_da_indovinare:
        print("Troppo basso, prova di nuovo!")
    elif tentativo > numero_da_indovinare:
        print("Troppo alto, prova di nuovo!")
    else:
        print(f"Complimenti! Hai indovinato il numero {numero_da_indovinare} in {tentativi} tentativi.")
        break
