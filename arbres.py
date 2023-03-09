class AB:
    def __init__(self, racine = None, gauche = None, droite = None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

    # Override de la méthode str pour afficher les attributs de l'objet
    def __str__(self):
        return f"Racine : {self.racine}\nGauche : {self.gauche}\nDroite : {self.droite}"

    def setGauche(self, gauche):
        self.gauche = gauche

    def setDroite(self, droite):
        self.droite = droite

    def setRacine(self, racine):
        self.racine = racine

    def getGauche(self):
        return self.gauche

    def getDroite(self):
        return self.droite

    def getRacine(self):
        return self.racine

    def estVide(self):
        if self.racine == None and self.gauche == None and self.droite == None:
            return True
        else:
            return False

    def taille(self):
        if self.estVide():
            return 0
        else:
            return 1 + self.gauche.taille() + self.droite.taille()
            

# Default values
# A1 = AB(None, None, None)

# A3 = AB(3, None, None)

# A2 = AB(5, A3, None)

#           Arbre a représente l'arbre suivant :
#
#                   10
#                 /    \
#                5      12
#               / \
#              3   8   
#

A1 = AB(5, 3, 8)

A2 = AB(12)

# A3 = AB(5, None, None)

Atest = AB(10, A1, A2)

# Atest.estVide() 

print(Atest.taille())


# A1.estVide()

# A2.estVide()




