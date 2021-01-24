#Dato un elenco di nazioni contenuto in una lista e uno delle rispettive capitali in una seconda lista (nazione 
#e relativa capitale si trovano nella medesima posizione delle rispettive liste), visualizza la capitale di una
#nazione della quale viene fornito da tastiera il nome, segnandolo con un messaggio di errore nel caso in cui la nazione richiesta non sia compresa nell'elenco.
nazioni = ["PORTOGALLO", "SPAGNA", "ITALIA", "FRANCIA", "GERMANIA", "INGHILTERRA"] 
capitali = ["Lisbona", "Madrid", "Roma", "Parigi", "Berlino", "Londra"]
nazione = input("Inserire il nome della nazione della quale si vuole sapere la capitale: ").upper()

if nazione in nazioni:
    index = nazioni.index(nazione)
    print("La capitale è", capitali[index])
else:
    print("ERRORE: nazione non presente nell'elenco.")
