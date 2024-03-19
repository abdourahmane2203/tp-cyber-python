class Etudiant:
    #Creation d'un constructeur - permet l'instanciation de la classe
    # Constructeur est une fonction
    # self designe l'objet courant.
    etudiant_cree = 0 # Variable de classe. une variable independante de tout objet de cette classe
    
    def __init__(self, nom, prenom, age, niveau):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.niveau = niveau
        Etudiant.etudiant_cree += 1
        
        print(f"Creation de l'étudiant {Etudiant.etudiant_cree}")
    
    def infos(self):
        print(f"Nom: {self.nom}, prénom: {self.prenom}, age: {self.age} ans, niveau d'étude: {self.niveau}") 
        print("-------------------------------------------------------------------------")
    

# Création d'un objet : création d'un étudiant.
print("-----------------------------------------------------------------------") 
e1 = Etudiant("Labrie", "Stéphane", 40, "AEC") 
e1.infos()

e2 = Etudiant("Diallo", "Abdou", 40, "Maitrise") 
e2.infos()

e3 = Etudiant("Bijou", "Jojo", 40, "Bacc") 
e3.infos()

e4 = Etudiant("St-Piere", "Maxime", 40, "Doctorat") 
e4.infos()