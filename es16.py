#Risolvi il problema precedente partendo da due liste che generano un dizionario con la nazione come chiave e la capitale come valore. 
#Successivamente interroga il dizionario per visualizzare la capitale di una nazione.
nazioni = ["PORTOGALLO", "SPAGNA", "ITALIA", "FRANCIA", "GERMANIA", "INGHILTERRA"] 
capitali = ["Lisbona", "Madrid", "Roma", "Parigi", "Berlino", "Londra"]
d = {}

for chiave in range(len(nazioni)):
    d[nazioni[chiave]] = capitali[chiave]

nazione = input("Inserire il nome della nazione della quale si vuole sapere la capitale: ")
risposta = nazione.upper()

if risposta in nazioni:
    print("La capitale è", d[risposta])
else:
    print("ERRORE: nazione non presente nell'elenco.")
