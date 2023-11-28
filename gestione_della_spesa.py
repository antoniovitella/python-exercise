def gestore_spese():
    spese_giornaliere = []  # Lista delle spese giornaliere

    while True:
        print("\nGestore Spese Giornaliere")
        print("1. Aggiungi spesa")
        print("2. Visualizza totale spese")
        print("3. Esci")

        scelta = input("Scelta: ")

        if scelta == '1':
            try:
                spesa = float(input("Inserisci l'importo della spesa: "))
                spese_giornaliere.append(spesa)
                print("Spesa aggiunta con successo!")
            except ValueError:
                print("Inserisci un importo valido.")

        elif scelta == '2':
            if not spese_giornaliere:
                print("Non ci sono spese registrate.")
            else:
                totale_spese = sum(spese_giornaliere)
                print(f"Il totale delle spese giornaliere è: {totale_spese:.2f}")

        elif scelta == '3':
            print("Grazie per aver utilizzato il Gestore Spese.")
            break

        else:
            print("Scelta non valida. Inserisci un numero da 1 a 3.")

# Esegui il gestore delle spese
gestore_spese()
