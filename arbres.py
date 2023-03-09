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

    # La taille d'un arbre est le nombre de noeuds de l'arbre
    def taille(self):
        taille = 0
        if self.getGauche() != None:
            taille += self.getGauche().taille()
        if self.getDroite() != None:
            taille += self.getDroite().taille()
        return taille + 1

    # Parcours prefixe : on visite la racine, puis le sous-arbre gauche, puis le sous-arbre droit
    def prefixe(self):
        parcours_prefixe = ""
        if self.getGauche() != None:
            parcours_prefixe += self.getGauche().prefixe()
        if self.getDroite() != None:
            parcours_prefixe += self.getDroite().prefixe()
        parcours_prefixe += str(self.getRacine()) + " "
        return parcours_prefixe

    # La hauteur d'un arbre est la longueur du plus long chemin entre la racine et une feuille
    def hauteur(self):
        hauteur = 0
        if self.getGauche() != None:
            hauteur += self.getGauche().hauteur()
        if self.getDroite() != None:
            hauteur += self.getDroite().hauteur()
        return hauteur + 1

    # ABR = Arbre Binaire de Recherche 
    # soit un arbre binaire dont les valeurs des noeuds de l'arbre sont ordonnées
    def estABR(self):
        if self.getGauche() != None:
            if str(self.getGauche().getRacine()) > str(self.getRacine()):
                return False
            else:
                self.getGauche().estABR()
        if self.getDroite() != None:
            if str(self.getDroite().getRacine()) < str(self.getRacine()):
                return False
            else:
                self.getDroite().estABR()
        return True

    # Un arbre binaire est équilibré si la différence de hauteur 
    # entre les sous-arbres gauche et droit est inférieure ou égale à 1
    def estEquilibre(self):
        if self.getGauche() != None:
            self.getGauche().estEquilibre()
        if self.getDroite() != None:
            self.getDroite().estEquilibre()
        if self.getGauche() != None and self.getDroite() != None:
            if self.getGauche().hauteur() - self.getDroite().hauteur() > 1:
                return False
        return True
        

# A3 = AB(3)

# A2 = AB(5, A3)

#           Arbre a représente l'arbre suivant :
#
#                   10
#                 /    \
#                5      12
#               / \
#              3   8   
#

#
A1 = AB(5, AB(3), AB(8))

A2 = AB(12)

A3 = AB(5)

Atest = AB(10, AB(A1), AB(A2))

# Verifions que les méthodes fonctionnent bien
# print(Atest.estVide())

# print(Atest.taille())

# print(Atest.hauteur())

print(Atest.prefixe())

# print(Atest.estABR())

# print(Atest.estEquilibre())

# A1.estVide()

# A2.estVide()
