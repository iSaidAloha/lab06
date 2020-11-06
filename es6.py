'''

Scrivete un programma che converta un numero romano, come MCMLXXVIII, nella
sua rappresentazione decimale.

Suggerimento. Per prima cosa, scrivete una funzione
che restituisce il valore numerico di ciascuna singola lettera, poi usate l’algoritmo
seguente:

totale = 0
Finché la stringa s contenente il numero romano non è vuota

Se valore(primo carattere di s) è almeno uguale a valore(secondo carattere
di s) oppure s ha lunghezza 1
    Aggiungi valore(primo carattere di s) a totale.
    Elimina il primo carattere di s.
Altrimenti
    Aggiungi a totale la differenza valore(secondo carattere di s) –
    valore(primo carattere di s)
    Elimina il primo e il secondo carattere di s

'''


def roman2arab(roman):
    if   roman == 'I': arab = 1
    elif roman == 'V': arab = 5
    elif roman == 'X': arab = 10
    elif roman == 'L': arab = 50
    elif roman == 'C': arab = 100
    elif roman == 'D': arab = 500
    elif roman == 'M': arab = 1000
    return arab


continue_ = 'Y'

while continue_ == 'Y':

    roman = input("Inserisci il numero romano ").strip()
    arab = 0

    while roman != "":

        if len(roman) == 1 or roman2arab(roman[0]) >= roman2arab(roman[1]):
            arab += roman2arab(roman[0])
            roman = roman[1:]
        else:
            arab += roman2arab(roman[1]) - roman2arab(roman[0])
            roman = roman[2:]

    print("Numero arabo = "+str(arab))

    continue_ = input("Continue? [Y/N] ").strip()

    if continue_ == 'N':
        print("Bye bye... 😢")

