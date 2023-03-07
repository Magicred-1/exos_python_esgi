from math import sqrt

# Premier Breakpoint
# Exercice 1
def calculVitesse(temps: int, distance: int):
    res = (distance / temps)

    return res

# print(calculVitesse(2, 100))

# Exercice 2
def saisirNomEtAge():
    nom: str = input("Quel est votre nom ? ")
    age: int = int(input("Quel est votre âge ? "))
    print("Bonjour " + nom + ", vous avez " + str(age) + " ans.")

# saisirNomEtAge()

# Exercice 3
def flottant(nombre: float):
    if nombre > 0 or nombre == 0:
        print(sqrt(nombre))
    else:
        print(f"Erreur : Le nombre {nombre} est négatif.")

# flottant(4)
# flottant(-2)

# Exercice 4
def lexicographique(mot1: str, mot2: str):
    if mot1 < mot2:
        print(mot1)
    elif mot2 < mot2:
        print(mot2)
    else:
        print(f"Les mots {mot1} & {mot2} sont identiques en taille.")

# lexicographique("bonjour", "bonsoir")
# lexicographique("bonjour", "bonjour")

# Exercice 5
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

# Deuxième Breakpoint

# Exercice 6
def verifierSaisie():
    arobase = "@"
    com = ".com"
    saisie: str = input("Saisissez votre adresse mail : ")

    if arobase in saisie and com in saisie:
        print("Adresse mail valide")

# verifierSaisie()

# Exercice 7
def afficherDixMessage(message: str):
    for i in range(10):
        print(message)

# afficherDixMessage("Bonjour")

# Exercice 8
def afficherMessageLettreParLettre(message: str):
    for i in message:
        print(i)

# afficherMessageLettreParLettre("Bonjour je suis un message")

# Exercice 9
def increment(a: int = 0, b: int = 10):
    while a < b:
        for i in range(a, b):
            print(i)

# increment()

# Exercice 10
def desincrement(b: int = 10):
    while b > 0:
        for i in range(b):
            b -= 1
            if b % 2 == 1:
                print(b)

# desincrement()

# Exercice 11
def saisieFiltreEntier(entier: int):
    if entier >= 1 and entier <= 10:
        print(entier)

# saisieFiltreEntier(5)
# saisieFiltreEntier(11)

# Exercice 12 & 13
def afficherCaracteresChaine(chaine: str, liste: list):
    for i in chaine:
        print(i)

    for j in range(0, len(liste), 3):
        print(liste[j])

    for k in range(0, len(liste), 2):
        if liste[k] % 2 == 0:
            print(liste[k])

afficherCaracteresChaine("Bonjour", [34, 56, 78, 90, 245, 456, 3553])

