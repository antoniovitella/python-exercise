# Dichiarazione variabile dj
dj = "DVS1"
    
# Descrizione stile musicale del dj
Descrizione =f"{dj} è uno dei DJ più venerati al mondo, voce di spicco nella preservazione della vera club culture si basa su un amore onnicomprensivo per la musica, un profondo rispetto per la sua arte e le esperienze nella scena rave del Midwest degli anni '90."

#Stampa la descrizione
print(Descrizione)

# Lista di famose location delle Boiler Room
location_boiler_room = [
    {"nome": "Berlino", "descrizione": "Berlino è stata sede di molte esibizioni leggendarie delle Boiler Room, celebre per la sua scena musicale elettronica e le location underground."},
    {"nome": "Londra", "descrizione": "Londra è stata una delle prime location delle Boiler Room, con eventi che hanno contribuito a plasmare la cultura musicale della città."},
    {"nome": "Tokyo", "descrizione": "Tokyo ha ospitato diverse esibizioni delle Boiler Room, offrendo un mix unico di influenze musicali tra tradizione e modernità."},
]

# Stampare ogni location con una breve descrizione o evento memorabile
for location in location_boiler_room:
    print(f"Location: {location['nome']}")
    print(f"Descrizione: {location['descrizione']}")
    print("-----------------------------")

# Chiedi all'utente di scegliere tra due generi musicali
genere_musicale = input("Scegli tra techno e EDM:")

# Verifica la scelta dell'utente e stampa un risultato diverso
if genere_musicale == "techno":
    print("Hai scelto il genere techno! La techno è un genere musicale nato alla fine degli anni '80, originario di Detroit, negli Stati Uniti. È caratterizzato da ritmi elettronici distinti, bassi profondi, linee di basso pulsanti e l'uso creativo di sintetizzatori e campionamenti.La sua essenza è spesso definita da un sound meccanico, astratto e ipnotico che mira a trasportare l'ascoltatore in un viaggio sonoro. Il techno è noto per la sua natura pulsante e per la sua capacità di creare un'atmosfera di energia costante che invita al movimento e alla danza.")
elif genere_musicale == "edm":
    print("Hai scelto il genere EDM! L'EDM (Electronic Dance Music) è un genere musicale che abbraccia una vasta gamma di stili e sottogeneri musicali all'interno della musica elettronica. Caratterizzato da ritmi elettronici, bassi profondi, melodie coinvolgenti e spesso accompagnato da elementi di sintetizzatori, l'EDM è noto per la sua natura energica e adatta alla pista da ballo.")
else:
    print("Scelta non valida. Si prega di selezionare tra techno e EDM.")
    
# Libreria dei DJ con le loro migliori tracce
libreria_dj = {
    "DVS1": [
        {"traccia": "Delta Wave", "link": "https://www.youtube.com/watch?v=gt2USPLK1AA"},
        {"traccia": "Black Russian", "link": "https://www.youtube.com/watch?v=q0EhhWxFdWs"}
    ],
    "Aphex Twin": [
        {"traccia": "T69 Collapse", "link": "https://www.youtube.com/watch?v=SqayDnQ2wmw"},
        {"traccia": "Xtal", "link": "https://www.youtube.com/watch?v=2tOutF8B3f8"}
    ],
    # Aggiungi altri DJ e le loro migliori tracce
}

# Stampare i DJ presenti nella libreria
print("Ecco alcuni DJ nella libreria:")
for dj in libreria_dj:
    print("-", dj)

# Chiedere all'utente di scegliere un DJ dalla lista
scelta_dj = input("\nScegli un DJ dalla lista: ")

# Verifica se il DJ scelto è presente nella libreria e stampa le sue migliori tracce
if scelta_dj in libreria_dj:
    migliori_tracce = libreria_dj[scelta_dj]
    print(f"Le migliori tracce di {scelta_dj} sono:")
    for traccia in migliori_tracce:
        print("-", traccia)
else:
    print("Il DJ selezionato non è presente nella lista.")
    
# Dizionario che mappa le location ai DJ che si sono esibiti lì
location_dj={
"chlär" : "Berlin",
"answer code request":"Berlin",
"object": "Berlin", 
"loefah": "London",
"burial": "London",
"djrum":"London",
"aphex twin": "Tokyo",
"kode9": "Tokyo", 
"kyoka": "Tokyo",
# Aggiungi altre location e i relativi DJ che si sono esibiti
}

print("Ecco alcuni DJ nella libreria:")
for dj in location_dj:
    print("-", dj)

# Funzione che restituisce il DJ famoso per una specifica location
def trova_location_per_dj(location):
    if location in location_dj:
        return location_dj[location]
    else:
        return "Nessun DJ famoso trovato per questa location"

# Test della funzione con una location a scelta
dj_test = input("Inserisci il nome del dj:")
location_trovata = trova_location_per_dj(dj_test)
print(f"{dj_test} si è esibitobnella seguente location: {location_trovata}")

# Dizionario che mappa le location ai DJ che si sono esibiti lì
location_dj = {
    "chlär": "Berlin",
    "answer code request": "Berlin",
    "object": "Berlin",
    "loefah": "London",
    "burial": "London",
    "djrum": "London"
    "aphex twin""Tokyo", # Questa riga mi da problemi con i ':'
    "kode9": "Tokyo",
    "kyoka": "Tokyo"
    # Altri DJ e location
}

# Richiesta all'utente di inserire la location di interesse
location_interesse = input("Inserisci la location di interesse: ")

# Utilizzo della comprensione delle liste per estrarre i DJ che si sono esibiti nella location specificata
dj_location_specifica = [dj for dj, location in location_dj.items() if location == location_interesse]

# Stampa dei DJ che si sono esibiti nella location specificata
print(f"I DJ che si sono esibiti a {location_interesse}:")
print(dj_location_specifica)


            