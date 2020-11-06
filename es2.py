'''

Scrivete la funzione:

def countWords(string)

che restituisca il numero di parole presenti nella stringa string. Le parole sono
sequenze di caratteri separate da spazi. Ad esempio, countWords(“Mary had a little
lamb”) restituisce 5.

'''


def countWords(string):
    string = string.strip()
    if string == '':
        return 0
    string = string+(' ')
    wrdCounter = 0
    for i in string:
        if i == ' ':
            wrdCounter += 1
    return int(wrdCounter)


continue_ = 'Y'

while continue_ == 'Y':

    string = input("Stringa? ")
    nWords = countWords(string)
    print("Le parole nella stringa sono "+str(nWords))

    continue_ = input("Continue? [Y/N] ").strip()

    if continue_ == 'N':
        print("Bye bye... 😢")
