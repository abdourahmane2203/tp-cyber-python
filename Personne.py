class Personne:
    """
    Cette classe personne nous permet de represennter la conception d'une personne 
    """
    personne_creee = 0
    # constructeur __init__()
    
    def __init__(self, nom, prenom, age): #-> None:
        self.__nom = nom # privé
        self.prenom = prenom # public
        self.__age = age # privé
        Personne.personne_creee += 1
    
    #Acceder a l'attribut age à l'exterieur de la classe
    def get_age(self):
        return self.__age

    # Mutatteur de l'attribut age 
    def set_age(self, age):
        self.__age = age

        #print("Personne créee : cela veut qu'un objet personne a été crée, Inanciation de la classe personne")
    def infos(self):
        print("........................................................")
        print(f"Nom: {self.__nom}, Prénom: {self.prenom}, Age: {self.__age}")



# main -> programme principal 
# Inanciation de la classe personne --> creation d'un objet personne : p1
print("-------------------------------------------")        
p1 = Personne("Labrie", "Stephane", 25) #p1
p1.infos()
# Non recommander en POO
# Encapulation ... 
p1.set_age(49)
print("Age access :", p1.get_age())
p1.prenom = "Jojo"
p1.__nom = "Bijou"
print("\nApres modification de l'age de stephane\n")
p1.infos()
p2 = Personne("Diallo", "Abdou", 14) #p2
p2.infos()
#p3 = Personne() #p3
#print(p1.__doc__)

print("-------------------------------------------") 