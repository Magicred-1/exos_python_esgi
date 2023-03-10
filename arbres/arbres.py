class AB:
    def __init__(self, racine = [None], gauche = None, droite = None):
            self.racine = racine
            self.gauche = gauche
            self.droite = droite


    # Override de la méthode str pour afficher les attributs de l'objet
    def __str__(self):
        return "Racine : {}\n Gauche :\n\t\t {}\n Droite :{} \n\t\t".format(self.racine, self.gauche, self.droite)

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
        if self.racine == [None]:
            return True
        return False
        
    # La taille d'un arbre est le nombre de noeuds de l'arbre
    def taille(self):
        if self.estVide():
            return 0
        taille = 0
        if self.getGauche() is not None:
            taille += self.getGauche().taille()
        if self.getDroite() is not None:
            taille += self.getDroite().taille()
        return taille + 1

    # Parcours prefixe : on visite la racine, puis le sous-arbre gauche, puis le sous-arbre droit
    def prefixe(self):
        if self.estVide():
            return []
        prefixe = [self.getRacine()]
        if self.getGauche() is not None:
            prefixe += self.getGauche().prefixe()
        if self.getDroite() is not None:
            prefixe += self.getDroite().prefixe()
        return prefixe

    # 
    def infixe(self):
        if self.estVide():
            return []
        infixe = []
        if self.getGauche() is not None:
            infixe += self.getGauche().infixe()
        infixe.append(int(self.getRacine()))  # cast to integer before appending
        if self.getDroite() is not None:
            infixe += self.getDroite().infixe()
        return infixe

    def postfixe(self):
        if self.estVide():
            return []
        postfixe = []
        if self.getGauche() is not None:
            postfixe += self.getGauche().postfixe()
        if self.getDroite() is not None:
            postfixe += self.getDroite().postfixe()
        postfixe.append(self.getRacine())
        return postfixe

    # La hauteur d'un arbre est la longueur du plus long chemin entre la racine et une feuille
    def hauteur(self):
        if self.estVide():
            return -1

        hauteur_gauche = self.getGauche().hauteur() if self.getGauche() is not None else -1
        hauteur_droite = self.getDroite().hauteur() if self.getDroite() is not None else -1

        return 1 + max(hauteur_gauche, hauteur_droite)

    # Une rotation à gauche consiste à faire monter le fils droit de la racine à la place de la racine
    def rotationGauche(self):
        if self.getDroite() != None:
            self.setRacine(self.getDroite().getRacine())
            self.setDroite(self.getDroite().getDroite())
            self.setGauche(AB(self.getRacine(), self.getGauche(), self.getDroite().getGauche()))
            self.getDroite().setGauche(self.getDroite().getDroite())
            self.getDroite().setDroite(None)
            return self

    # Une rotation à droite consiste à faire monter le fils gauche de la racine à la place de la racine
    def rotationDroite(self):
        if self.getGauche() != None:
            self.setRacine(self.getGauche().getRacine())
            self.setGauche(self.getGauche().getGauche())
            self.setDroite(AB(self.getRacine(), self.getGauche().getDroite(), self.getDroite()))
            self.getGauche().setDroite(self.getGauche().getGauche())
            self.getGauche().setGauche(None)
            return self
    

    # ABR = Arbre Binaire de Recherche 
    # soit un arbre binaire dont les valeurs des noeuds de l'arbre sont ordonnées
    def estABR(self):
        if self.getGauche() != None:
            if self.getGauche().getRacine() > self.getRacine():
                return False
            else:
                self.getGauche().estABR()
        if self.getDroite() != None:
            if self.getDroite().getRacine() < self.getRacine():
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
        

if __name__ == "__main__":
#   Arbre a représenter l'arbre suivant :
#
#                   10
#                 /    \
#                5      12
#               / \
#              3   8  
#             /     \
#            5       16

    A1 = AB(5, AB(3,AB(5), AB(16)), AB(8))

    A2 = AB(12)

    A3 = AB(10, A1, A2)


    print(f"Prefixe : {A3.prefixe()}")

    print(f"Infixe : {A3.infixe()}")

    print(f"Postfixe : {A3.postfixe()}")

    print(f"Taille : {A3.taille()}")

    print(f"Hauteur : {A3.hauteur()}")

    print(f"Est équilibré : {A3.estEquilibre()}")

    print(f"Est ABR : {A3.estABR()}")

    print(f"Rotation droite : {A3.rotationDroite()}")

    print(f"Rotation gauche : {A3.rotationGauche()}")
