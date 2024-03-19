"""
Exercice : Gestion d'une Librairie
Écrivez une classe Livre pour représenter un livre dans une librairie. Chaque livre devrait avoir les attributs suivants :
Titre
Auteur
Genre
Prix
La classe Livre devrait également avoir les méthodes suivantes :
Un constructeur pour initialiser les attributs du livre.
Des méthodes getters et setters pour chaque attribut.
Une méthode afficher_details() pour afficher les détails du livre (titre, auteur, genre, prix).
Ensuite, créez une classe Librairie pour représenter une collection de livres. La classe Librairie devrait avoir les attributs suivants :
Un dictionnaire pour stocker les livres, où la clé est le titre du livre et la valeur est une instance de la classe Livre.
La classe Librairie devrait également avoir les méthodes suivantes :
Une méthode ajouter_livre() pour ajouter un livre à la collection.
Une méthode supprimer_livre() pour supprimer un livre de la collection.
Une méthode chercher_livre() pour rechercher un livre par son titre et afficher ses détails.
Testez ensuite votre code en créant une instance de la classe Librairie, en ajoutant quelques livres, en supprimant un livre, et en recherchant un livre par son titre.
"""
class Livre:
    def __init__(self, titre, auteur, genre, prix):
        self.__titre = titre
        self.__auteur = auteur
        self.genre = genre
        self.__prix = prix

    #Titre
    def get_titre(self):
        return self.__titre
    def set_titre(self, titre):
        self.__titre = titre
   
    #Auteur 
    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, auteur):
        self.__auteur =  auteur

    #Genre
    def get_genre(self):
        return self.genre
    def set_genre(self, genre):
        self.genre = genre 

    #Prix
    def get_prix(self):
        return self.__prix
    def set_prix(self, prix):
        self.__prix = prix

    def afficher_details(self):
        print(self.get_titre())
        print(self.get_auteur())  
        print(self.get_genre())  
        print(self.get_prix())

livre1 = Livre("PHP","Labrie", "Informatique", 110)  
livre1.afficher_details()         

class Librairie:
    def __init__(self):
        self.livres = {}
    
    def ajouter_livre(self, livre):
        tittre = livre.get_titre()
        self.livres[tittre] = livre
    
    def afficher_librairie(self):
        for titre,livre in self.livres.items():
            print("-----------------------------------------------")
            print(f"{titre} -> {livre.get_auteur()}, {livre.get_genre()}, {livre.get_prix()}")

    def supprimer_livre(self, titre):
        if titre in self.livres:
            del self.livres[titre]
            print(f"{titre}, ce livre a été bien supprimé de la collection")  
        else:
            print(f"Le livre {titre} n'est pas trouvé")

    def chercher_livre(self, titre):
        titre = titre.lower()
        if titre in self.livres:
            self.livres[titre].afficher_details()
        else:
           print(f"Le livre {titre} n'est pas trouvé")   


# Mian
librairie = Librairie()           

livre1 = Livre("python", "Labrie", "Informatique", 120)
livre2 = Livre("python3", "Stephane", "Informatique", 125)
livre3 = Livre("php", "Labrie", "Informatique", 110)

librairie.ajouter_livre(livre1)
librairie.ajouter_livre(livre2)
librairie.ajouter_livre(livre3)

librairie.afficher_librairie()
print("-----------------------------------------------")

librairie.chercher_livre("PHP")
librairie.supprimer_livre("php")

librairie.afficher_librairie()
print("-----------------------------------------------")
