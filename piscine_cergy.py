from math import sqrt

# Premier Breakpoint
def calculVitesse(temps: int, distance: int):
    res = (distance / temps)

    return res

# print(calculVitesse(2, 100))

def saisirNomEtAge():
    nom: str = input("Quel est votre nom ? ")
    age: int = int(input("Quel est votre âge ? "))
    print("Bonjour " + nom + ", vous avez " + str(age) + " ans.")

# saisirNomEtAge()

def flottant(nombre: float):
    if nombre > 0 or nombre == 0:
        print(sqrt(nombre))
    else:
        print(f"Erreur : Le nombre {nombre} est négatif.")

# flottant(4)
# flottant(-2)

def lexicographique(mot1: str, mot2: str):
    if mot1 < mot2:
        print(mot1)
    elif mot2 < mot2:
        print(mot2)
    else:
        print(f"Les mots {mot1} & {mot2} sont identiques en taille.")

# lexicographique("bonjour", "bonsoir")
# lexicographique("bonjour", "bonjour")

def enceintePressurisee():
    pSeuil = 2.3
    vSeuil = 7.41

    pression: int = int(input("Quelle est la pression ? "))
    volume: int = int(input("Quelle est le volume ? "))

    if pression and volume > 0:
        if pression > pSeuil and volume > vSeuil:
            print("arrêt immédiat")
        elif pression > pSeuil:
            print("Veuillez augmenter le volume")
        elif volume > vSeuil:
            print("Veuillez augmenter la pression")
        else:
            print("tout va bien")

# enceintePressurisee()
