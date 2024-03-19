class Livre:
    def __init__(self, titre, auteur, genre, prix):
        self.titre = titre
        self.auteur = auteur
        self.genre = genre
        self.prix = prix

    def afficher_details(self):
        print("Titre:", self.titre)
        print("Auteur:", self.auteur)
        print("Genre:", self.genre)
        print("Prix:", self.prix)

class Librairie:
    def __init__(self):
        self.livres = {}

    def ajouter_livre(self, livre):
        self.livres[livre.titre] = livre

    def supprimer_livre(self, titre):
        del self.livres[titre]

    def chercher_livre(self, titre):
        if titre in self.livres:
            print("Détails du livre recherché :")
            self.livres[titre].afficher_details()
        else:
            print("Livre non trouvé dans la librairie.")

# Test du code
librairie = Librairie()

# Ajout de livres
livre1 = Livre("Le Seigneur des Anneaux", "J.R.R. Tolkien", "Fantasy", 25.99)
livre2 = Livre("Harry Potter à l'école des sorciers", "J.K. Rowling", "Fantasy", 19.99)

librairie.ajouter_livre(livre1)
librairie.ajouter_livre(livre2)

# Recherche d'un livre
librairie.chercher_livre("Le Seigneur des Anneaux")

# Suppression d'un livre
librairie.supprimer_livre("Harry Potter à l'école des sorciers")

# Recherche d'un livre après suppression
librairie.chercher_livre("Harry Potter à l'école des sorciers")