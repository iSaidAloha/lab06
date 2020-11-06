'''

Un’organizzazione non governativa ha bisogno di un programma per calcolare la
quota di sussidio economico da assegnare a ciascuna famiglia bisognosa di
assistenza. La formula è la seguente:

    • Se il reddito annuo della famiglia è compreso tra $ 30 000 e $ 40 000 e la
    famiglia ha almeno tre fi gli, il sussidio è pari a $ 1000 per ogni figlio.
    • Se il reddito annuo della famiglia è compreso tra $ 20 000 e $ 30 000 e la
    famiglia ha almeno due fi gli, il sussidio è pari a $ 1500 per ogni figlio.
    • Se il reddito annuo della famiglia è minore di $ 20 000, il sussidio è pari a $
    2000 per ogni figlio.

Scrivete una funzione che faccia questi calcoli, poi scrivete un programma che
chieda all’utente di fornire il reddito annuo e il numero di figli di ciascuna famiglia
richiedente il sussidio, visualizzando il valore corrispondentemente restituito dalla
funzione. Usate –1 come valore sentinella per terminare l’immissione dei dati.

'''


def subsidy(money, sons):
    if 30000 <= money < 40000 and sons >= 3:
        subXson = 1000
    elif 20000 <= money < 30000 and sons >= 2:
        subXson = 1500
    elif money < 20000:
        subXson = 2000
    else:
        subXson = 0

    return subXson * sons


continue_ = 'Y'

while continue_ == 'Y':

    figli = int(input("Quanti figli hai? ").strip())
    soldi = int(input("Quanto è il tuo reddito annuo? ").strip())

    sussidio = subsidy(soldi, figli)

    print(f"Ti spetta un sussidio di {sussidio}€ 💸")

    continue_ = input("Continue? [Y/N] ").strip()

    if continue_ == 'N':
        print("Bye bye... 😢")
