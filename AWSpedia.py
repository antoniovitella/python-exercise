import csv
import json


with open('Categorie.csv', newline='') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        # Supponendo che la prima riga del CSV contenga i nomi delle colonne
        key = row['Name']  # Cambia 'column_name' con il nome della colonna chiave
        data[key] = row

# Scrivi il dizionario convertito in JSON in un file
with open(json_file_path, 'w') as jsonfile:
    json.dump(data, jsonfile, indent=4)
