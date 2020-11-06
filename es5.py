'''

Scrivete una funzione che calcoli il saldo di un conto bancario dopo che siano
trascorsi un dato numeri di anni, a partire da un dato saldo iniziale e con un dato
tasso di interesse annuo, accreditando gli interessi annualmente.

'''


def fMoney(smoney, years, interest):
    for i in range(years):
        smoney += smoney * interest/100
    return round(smoney, 2)


continue_ = 'Y'

while continue_ == 'Y':

    iSaldo = int(input("A quanto ammonta il saldo iniziale? ").strip())
    anni = int(input("Per quanti anni maturerà il tuo saldo? ").strip())
    interesse = int(input("A quanto ammonta l'interesse annuale? (in %) ").strip())

    fSaldo = fMoney(iSaldo, anni, interesse)
    print(f"Il saldo, trascorsi {anni} anni, con un interesse del {interesse}%, sarà di {fSaldo}€")

    continue_ = input("Continue? [Y/N] ").strip()

    if continue_ == 'N':
        print("Bye bye... 😢")
