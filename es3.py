'''

Scrivete una funzione,

find(string, match),

che verifichi se la stringa match è
contenuta nella stringa string:

b = find(“Mississippi”, “sip”) # Assegna a b il valore True

'''


def find(string, match):
    if match in string:
        return True
    else:
        return False


continue_ = 'Y'

while continue_ == 'Y':

    string = input("Stringa? ").strip()
    match = input("Sotto-stringa? ").strip()
    if find(string, match):
        print(f"La sotto-stringa '{match}' è contenuta in '{string}'")
    else:
        print(f"La sotto-stringa '{match}' NON è contenuta in '{string}'")

    continue_ = input("Continue? [Y/N] ").strip()

    if continue_ == 'N':
        print("Bye bye... 😢")
