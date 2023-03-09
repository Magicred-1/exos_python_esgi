from math import sqrt
import random

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

# afficherCaracteresChaine("Bonjour", [34, 56, 78, 90, 245, 456, 3553])

# Exercice 15

def liste(liste = [17, 38, 10, 25, 72]):
    
    sorted(liste)

    print(f"La liste trié : {liste}\n")

    liste.append(12)

    print(f"La liste avec l'élément 12 : {liste}\n")

    liste.reverse()

    print(f"La liste inversé : {liste}\n")

    for i in range(0, len(liste)):
        if liste[i] == 17:
            print(f"La valeur 17 est à l'index {i}\n")

    liste.remove(38)

    print(f"La liste sans l'élément 38 : {liste}\n")

    print(f"La sous liste du 2ème au 3ème élément: {liste[1:3]}\n")

    print(f"La sous liste du 2ème au dernier élément: {liste[1:]}\n")

    print(f"La sous liste complète de la liste: {liste[:]}")

# liste()

# Exercice 16
def inverseChaine(chaine: str):
    print(chaine[::-1])

# inverseChaine("Bonjour")

# Exercice 17
def palindrome(chaine: str):
    if chaine == chaine[::-1]:
        print(f"{chaine} est un palindrome !")
    else:
        print(f"{chaine} n'est pas un palindrome !")

# palindrome("kayak")
# palindrome("moralez")

# Exercice 18
def chaineEmail(email: str):
    # contains @ and .com + 3 characters after .
    if "@" in email and "." and len(email[email.index(".") + 1:]) == 3:
        print(f"{email} est une adresse mail valide !")
    else:
        print(f"{email} n'est pas une adresse mail valide !")

# chaineEmail("djasongadiou@gmail.d")
# chaineEmail("papyfaitdelaresistance@gmail.com")

# Exercice 19
def iniatialisationListe():
    liste = []

    for i in range(5):
        liste.append(random.uniform(1.0, 10.0))

    return liste

# print(iniatialisationListe())

# Exercice 20
def affichageRange():
    for i in range(0, 3):
        print(i)

    for j in range(4, 7):
        print(j)

    for k in range(2, 8, 2):
        print(k)

    chose = [1, 2, 3, 4, 5]

    if 3 in chose and 6 in chose:
        print("3 et 6 sont dans chose")
    elif 3 in chose:
        print("3 est dans chose")

# affichageRange()