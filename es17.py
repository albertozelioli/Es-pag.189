#Costruisci un dizionario ottenuto da quello dell'esercizio precedente invertendo ruolo di chiave e valore.
#Usa il nuovo dizionario per trovare il nome della nazione, noto il nome della capitale.
nazioni = ["Portogallo", "Spagna", "Italia", "Francia", "Germania", "Inghilterra"] 
capitali = ["LISBONA", "MADRID", "ROMA", "PARIGI", "BERLINO", "LONDRA"]
d = {}

for valore in range(len(capitali)):
    d[capitali[valore]] = nazioni[valore]

capitale = input("Inserire il nome della capitale della quale si vuole sapere la nazione: ")
risposta = capitale.upper()

if risposta in capitali:
    print("La nazione è", d[risposta])
else:
    print("ERRORE: capitale non presente nell'elenco.")
