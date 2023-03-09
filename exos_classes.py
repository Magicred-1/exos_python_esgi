class Commande:
    def __init__(self, date: str, numero: int, prix: int = 0):
        self.date = date
        self.numero = numero
        self.prix = prix

    def acquitter(self):
            print("Commande acquittée")

    def calculTVA(self):
        return self.prix * 0.196

    def add(self, commande):
        commande.numero += self.numero + 1
        commande.prix += self.prix
        return commande

    # Override de la méthode str pour afficher les attributs de l'objet
    def __str__(self) -> str:
        return f"Commande {self.numero} du {self.date} pour un montant de {self.prix}€"

class CommandeAcquittee(Commande):
    def __init__(self, date: str, prix: int):
        super().__init__(date, prix)
        self.acquittee = True
        self.date = date
        self.prix = prix

    def acquitter(self):
        return self.date + " " + self.prix

class Client:
    def __init__(self, nom: str, adresse: str):
        self.nom = nom
        self.adresse = adresse

    def contacter(self):
        print(f"Vous avez contacté {self.nom} à l'adresse suivante : {self.adresse}")

client = Client("Jean", "1 rue de la paix")

client.contacter()

commande = Commande("01/01/2020", 1, 100)

# commande.acquitter()

commande2 = Commande("01/01/2020", 2, 100)

print(commande.add(commande2))

# Méthode consacrée à l'affichage d'un objet (__str__) pour overide str pour afficher les attributs de l'objet

command3 = CommandeAcquittee("01/01/2020", 100)

# print(command3)
        