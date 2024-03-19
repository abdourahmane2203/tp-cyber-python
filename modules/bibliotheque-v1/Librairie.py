class Librairie:
    def __init__(self):
        self.livres = {}
    
    def ajouter_livre(self, livre):
        titre = livre.get_titre()
        self.livres[titre] = livre
    
    def afficher_librairie(self):
        print("-----------------------------------------------")
        for titre,livre in self.livres.items():
            print(f"{titre} -> {livre.get_auteur()}, {livre.get_genre()}, {livre.get_prix()}")
            print("-----------------------------------------------")

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
