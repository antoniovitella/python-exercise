import csv
import json

# Conversione da CSV a JSON
with open('boilerroom.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    data = {'DJ': []}
    for row in reader:
        data['DJ'].append(row)

# Salvataggio del JSON in un file
with open('boilerroom.json', 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)

# Lettura e stampa del file JSON
with open('boilerroom.json', 'r') as jsonfile:
    json_data = json.load(jsonfile)
    print(json.dumps(json_data, indent=4))
# Trova e stampa le informazioni di un DJ specifico per nome
def trova_dj_per_nome(nome):
    with open('boilerroom.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        for dj in data['DJ']:
            if dj['nome'] == nome:
                print(dj)
                return

# Utilizzo della funzione per trovare un DJ specifico
trova_dj_per_nome("nome")
# Modifica la location o il genere musicale di un DJ e aggiorna il file JSON
def modifica_dj(nome, campo, nuovo_valore):
    with open('boilerroom.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        for dj in data['DJ']:
            if dj['nome'] == nome:
                dj[campo] = nuovo_valore

    # Salvataggio delle modifiche nel file JSON
    with open('boilerroom.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Esempio di modifica di un campo per un DJ specifico
modifica_dj('nome', 'location', 'genere')
# Aggiungi un nuovo DJ al file JSON
def aggiungi_nuovo_dj(nome, location, genere):
    with open('boilerroom.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        nuovo_dj = {'nome': nome, 'location': location, 'genere': genere}
        data['DJ'].append(nuovo_dj)

    # Salvataggio delle modifiche nel file JSON
    with open('boilerroom.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Esempio di aggiunta di un nuovo DJ
aggiungi_nuovo_dj('Solomun', 'Ibiza', 'House')
# Rimuovi un DJ dal file JSON in base al nome
def rimuovi_dj(nome):
    with open('boilerroom.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        data['DJ'] = [dj for dj in data['DJ'] if dj['nome'] != nome]

    # Salvataggio delle modifiche nel file JSON
    with open('boilerroom.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Esempio di rimozione di un DJ
rimuovi_dj('Nina Kraviz')
# Ordina i DJ nel file JSON per genere musicale in ordine alfabetico
def ordina_per_genere():
    with open('boilerroom.json', 'r') as jsonfile:
        data = json.load(jsonfile)
        data['DJ'] = sorted(data['DJ'], key=lambda x: x['genere'])

    # Salvataggio delle modifiche nel file JSON
    with open('boilerroom.json', 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Esempio di ordinamento dei DJ per genere musicale e salvataggio
ordina_per_genere()
