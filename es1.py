'''

Scrivete la funzione:
def countVowel(string)

che restituisca il numero di vocali presenti nella stringa string. Le vocali sono le
lettere a, e, i, o e u, oltre alle rispettive versioni maiuscole.

'''

vowels = ['a', 'e', 'i', 'o', 'u']

def countvowel(string):
    counter = 0
    for i in string:
        if i.lower() in vowels:
            counter += 1
    return int(counter)


continue_ = 'Y'

while continue_ == 'Y':

    string = input("Inserisci la stringa > ")
    nvowels = countvowel(string)
    print("Le vocali sono "+str(nvowels))

    continue_ = input("Continue? [Y/N] ").strip()

    if continue_ == 'N':
        print("Bye bye... 😢")
