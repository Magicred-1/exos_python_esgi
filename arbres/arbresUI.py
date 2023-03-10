import tkinter as tk
from arbres import AB
from drawtree import draw_level_order

# Fênetre pour créer un arbre
class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Génération d'arbres binaires")
        self.geometry("600x600")
        self.resizable(False, False)
        self.config(background="white", padx=20, pady=20)
        self.arbre = AB()
        self.createUI()

    def createUI(self):
        self.label = tk.Label(self, text="Création d'un arbre", font=("Arial", 20), bg="white")
        self.label.pack(pady=20)

        self.label_racine = tk.Label(self, text="Racine :", font=("Arial", 15), bg="white")
        self.label_racine.pack(pady=10)

        self.racine = tk.Entry(self, font=("Arial", 15))
        self.racine.pack(pady=10)

        self.label_gauche = tk.Label(self, text="Gauche :", font=("Arial", 15), bg="white")
        self.label_gauche.pack(pady=10)

        self.gauche = tk.Entry(self, font=("Arial", 15))
        self.gauche.pack(pady=10)

        self.label_droite = tk.Label(self, text="Droite :", font=("Arial", 15), bg="white")
        self.label_droite.pack(pady=10)

        self.droite = tk.Entry(self, font=("Arial", 15))
        self.droite.pack(pady=10)

        self.button = tk.Button(self, text="Créer l'arbre", font=("Arial", 15), bg="white", command=self.createTree)
        self.button.pack(pady=10)

        self.resultat = tk.Label(self, text="Résultat :", font=("Arial", 20), bg="white")

    def getTree(self):
        return self.arbre

    def createTree(self):
        if self.getTree() is not None:
            # incrementer le nombre d'arbre crée
            self.arbre = AB(self.racine.get(), AB(self.gauche.get()), AB(self.droite.get()))
        self.showTree()

    def showTree(self):
        if self.arbre.estVide():
            self.label_tree = tk.Label(self, text="L'arbre est vide", font=("Arial", 15), bg="white")
            self.label_tree.pack(pady=10)
        else:
            self.drawTree(self.arbre)
            self.label_tree = tk.Label(self, text="Le préfixe de l'arbre est :", font=("Arial", 15), bg="white")
            self.label_tree.pack(pady=10)
            self.resultat = tk.Label(self, text=self.arbre.stringPrefixe(), font=("Arial", 15), bg="white")
            self.resultat.pack(pady=10)

    def drawTree(self, arbre):
        if arbre.estVide():
            return
        else:
            draw_level_order(arbre.stringPrefixe())

    

if __name__ == "__main__":
    Windows().mainloop()
