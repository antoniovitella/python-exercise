def analizza_testo(testo):
    parole=testo.lower().split() #Converte il tyesto in minuscole e separa le parole
    numero_parole=len(parole) #Numero totale di parole
    frequenza_parole={}#Dizionario per tenere gtraccia della frequenza delle parole
    lunghezza_totale=0 #Inizializza la lunghezza totale delle parole
    
    #Calcola la frequenza di ogni parola e la lunghezza totale
    for parola in parole:
        if parola in frequenza_parole:
            frequenza_parole[parola] += 1
        else:
            frequenza_parole[parola] = 1
    #Calcola la lunghezza medi delle parole
    lunghezza_media = round(lunghezza_totale / numero_parole, 3) if numero_parole>0 else 0.0
    
    #Costruisci il dizionario con le informazioni richieste
    risultato = {
        'numero_pagine': numero_parole,
        'parole': frequenza_parole,
        'lunghezza_media': lunghezza_media
    }
    
    return risultato

testo = str(input("INSERISCI TESTO:"))
risultato = analizza_testo(testo)
print(risultato)

    