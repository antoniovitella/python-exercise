import random

def lancio_dado():
    return random.randint(1, 6)  # Genera un numero casuale da 1 a 6 (valori di un dado)

def gioco_dadi():
    input("Premi INVIO per lanciare i dadi...")
    
    # Lancio dei dadi per il giocatore 1
    dado1_giocatore1 = lancio_dado()
    dado2_giocatore1 = lancio_dado()
    punteggio_giocatore1 = dado1_giocatore1 + dado2_giocatore1

    print(f"Giocatore 1 ha ottenuto {dado1_giocatore1} e {dado2_giocatore1}, totale: {punteggio_giocatore1}")

    # Lancio dei dadi per il giocatore 2
    dado1_giocatore2 = lancio_dado()
    dado2_giocatore2 = lancio_dado()
    punteggio_giocatore2 = dado1_giocatore2 + dado2_giocatore2

    print(f"Giocatore 2 ha ottenuto {dado1_giocatore2} e {dado2_giocatore2}, totale: {punteggio_giocatore2}")

    # Determinazione del vincitore
    if punteggio_giocatore1 > punteggio_giocatore2:
        print("Giocatore 1 vince!")
    elif punteggio_giocatore2 > punteggio_giocatore1:
        print("Giocatore 2 vince!")
    else:
        print("È un pareggio!")

# Esegui il gioco
gioco_dadi()

