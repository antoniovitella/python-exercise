def gestore_lista_spesa():
    lista_spesa = []  

    while True:
        print("\nGestore Lista della Spesa")
        print("1. Aggiungi elemento")
        print("2. Rimuovi elemento")
        print("3. Visualizza lista della spesa")
        print("4. Esci")

        scelta = input("Scelta: ")

        if scelta == '1':
            nuovo_elemento = input("Inserisci un nuovo elemento: ")
            lista_spesa.append(nuovo_elemento)
            print("Elemento aggiunto alla lista della spesa!")

        elif scelta == '2':
            if not lista_spesa:
                print("La lista della spesa è vuota.")
            else:
                print("Lista della spesa attuale:")
                for idx, elemento in enumerate(lista_spesa, start=1):
                    print(f"{idx}. {elemento}")
                try:
                    indice_da_rimuovere = int(input("Inserisci il numero dell'elemento da rimuovere: "))
                    if 1 <= indice_da_rimuovere <= len(lista_spesa):
                        elemento_rimosso = lista_spesa.pop(indice_da_rimuovere - 1)
                        print(f"'{elemento_rimosso}' rimosso dalla lista della spesa.")
                    else:
                        print("Indice non valido.")
                except ValueError:
                    print("Inserisci un numero valido.")
        elif scelta == '3':
            if not lista_spesa:
                print("La lista della spesa è vuota.")
            else:
                print("Lista della spesa!")
                for idx, elemento in enumerate(lista_spesa, start=1):
                    print(f"{idx}. {elemento}")
        elif scelta == '4':
            print("Grazie per aver utilizzato il Gestore Lista della Spesa.")
            break
        else:
            print("Scelta non valida. Inserisci un numero da 1 a 4.")
# Esegui il gestore della lista della spesa
gestore_lista_spesa()
