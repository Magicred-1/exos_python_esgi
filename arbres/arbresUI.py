import tkinter as tk
from arbres import AB
import matplotlib.pyplot as plt

# Fênetre pour créer un arbre
class Windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Génération d'arbres binaires")
        self.geometry("1300x1300")
        self.resizable(False, False)
        self.config(background="white", padx=5, pady=5)
        self.arbre = AB()
        self.createUI()

    def createUI(self):
        self.label = tk.Label(self, text="Création d'un arbre", font=("Arial", 20), bg="white")
        self.label.pack(pady=5)

        self.label_racine = tk.Label(self, text="Racine :", font=("Arial", 15), bg="white")
        self.label_racine.pack(pady=5)

        self.racine = tk.Entry(self, font=("Arial", 15))
        self.racine.pack(pady=5)

        self.label_gauche = tk.Label(self, text="Gauche :", font=("Arial", 15), bg="white")
        self.label_gauche.pack(pady=5)

        self.gauche = tk.Entry(self, font=("Arial", 15))
        self.gauche.pack(pady=5)

        self.label_droite = tk.Label(self, text="Droite :", font=("Arial", 15), bg="white")
        self.label_droite.pack(pady=5)

        self.droite = tk.Entry(self, font=("Arial", 15))
        self.droite.pack(pady=5)

        self.button = tk.Button(self, text="Créer l'arbre", font=("Arial", 15), bg="white", command=self.showTreeInfos)
        self.button.pack(pady=5)

    def generateTree(self):
        # Créer arbre binaires avec les valeurs entrées par l'utilisateur
        plt.figure(figsize=(10, 10))
        plt.axis('off')
        plt.title("Arbre binaire", fontsize=20)
        plt.text(0.5, 0.5, self.racine.get(), fontsize=20, ha='center', va='center')
        plt.text(0.25, 0.25, self.gauche.get(), fontsize=20, ha='center', va='center')
        plt.text(0.75, 0.25, self.droite.get(), fontsize=20, ha='center', va='center')
        plt.show()

    def showTreeInfos(self):
        self.arbre = AB([self.racine.get()], AB([self.gauche.get()]), AB([self.droite.get()]))
        
        # Affichage de l'arbre
        self.label = tk.Label(self, text="Affichage de l'arbre", font=("Arial", 20), bg="white")
        self.label.pack(pady=5)

        self.label_taille = tk.Label(self, text=f"Taille de l'arbre : {self.arbre.taille()}", font=("Arial", 15), bg="white")
        self.label_taille.pack(pady=5)

        self.label_prefixe = tk.Label(self, text=f"Parcours préfixe : {self.arbre.prefixe()}", font=("Arial", 15), bg="white")
        self.label_prefixe.pack(pady=5)

        self.label_infixe = tk.Label(self, text=f"Parcours infixe : {self.arbre.infixe()}", font=("Arial", 15), bg="white")
        self.label_infixe.pack(pady=5)

        self.label_abr = tk.Label(self, text=f"Est un ABR ? : {self.arbre.estABR()}", font=("Arial", 15), bg="white")
        self.label_abr.pack(pady=5)
    
        self.label_equilibre = tk.Label(self, text=f"Equilibré ? : {self.arbre.estEquilibre()}", font=("Arial", 15), bg="white")
        self.label_equilibre.pack(pady=5)

        self.label_hauteur = tk.Label(self, text=f"Hauteur de l'arbre : {self.arbre.hauteur()}", font=("Arial", 15), bg="white")
        self.label_hauteur.pack(pady=5)
        
        self.generateTree()


if __name__ == "__main__":
    Windows().mainloop()
