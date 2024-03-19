
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

class ListePersonnes:
    def __init__(self):
        self.personnes = []

    def ajouter_personne(self, nom, age):
        personne = Personne(nom, age)
        self.personnes.append(personne)

    def afficher_personnes(self):
        for personne in self.personnes:
            print(f"Nom: {personne.nom}, Age: {personne.age}")

    def rechercher_personne(self, nom):
        for personne in self.personnes:
            if personne.nom == nom:
                print(f"Nom: {personne.nom}, Age: {personne.age}")
                return
        print(f"Aucune personne trouvée avec le nom {nom}.")

    def filtrer_personnes_par_age(self, min_age, max_age):
        for personne in self.personnes:
            if min_age <= personne.age <= max_age:
                print(f"Nom: {personne.nom}, Age: {personne.age}")

class FileAttente:
    def __init__(self):
        self.attente_normale = []
        self.attente_prioritaire = []

    def ajouter_personne_en_attente(self, nom):
        self.attente_normale.append(nom)

    def ajouter_personne_prioritaire(self, nom):
        self.attente_prioritaire.append(nom)

    def supprimer_personne_de_attente(self):
        if self.attente_prioritaire:
            personne = self.attente_prioritaire.pop(0)
        elif self.attente_normale:
            personne = self.attente_normale.pop(0)
        else:
            personne = None

        if personne:
            print(f"Personne supprimée de la file d'attente : {personne}")

class SalleCinema:
    def __init__(self, capacite, places_speciales):
        self.capacite = capacite
        self.places_disponibles = capacite
        self.reservations = []
        self.places_speciales = places_speciales

    def reserver_place(self, nom, place):
        if self.places_disponibles > 0:
            self.reservations.append((nom, place))
            self.places_disponibles -= 1
            print(f"Place réservée pour {nom} à la place {place}.")
        else:
            print("Désolé, plus de places disponibles.")

    def afficher_places_reservees(self):
        for reservation in self.reservations:
            print(f"{reservation[0]} a réservé la place {reservation[1]}.")

    def nombre_places_disponibles(self):
        print(f"Nombre de places disponibles : {self.places_disponibles}")

    def filtrer_reservations_par_personne(self, nom):
        reservations_personne = [place for personne, place in self.reservations if personne == nom]
        if reservations_personne:
            print(f"Réservations de {nom} : {', '.join(reservations_personne)}")
        else:
            print(f"Aucune réservation trouvée pour {nom}.")

    def annuler_reservation(self, nom):
        self.reservations = [(personne, place) for personne, place in self.reservations if personne != nom]
        print(f"Réservations annulées pour {nom}.")

    def reserver_place_speciale(self, nom):
        if self.places_speciales > 0:
            self.reservations.append((nom, f"Place spéciale {self.places_speciales}"))
            self.places_speciales -= 1
            print(f"Place spéciale réservée pour {nom}.")
        else:
            print("Désolé, plus de places spéciales disponibles.")

liste_personnes = ListePersonnes()
liste_personnes.ajouter_personne("Jonas", 25)
liste_personnes.ajouter_personne("Bernard", 30)
liste_personnes.afficher_personnes()
liste_personnes.rechercher_personne("Jonas")
liste_personnes.filtrer_personnes_par_age(5, 85)

file_attente = FileAttente()
file_attente.ajouter_personne_prioritaire("Charlie")
file_attente.ajouter_personne_en_attente("David")
file_attente.supprimer_personne_de_attente()

salle_cinema = SalleCinema(capacite=30, places_speciales=5)
salle_cinema.reserver_place("Jonas", "A1")
salle_cinema.reserver_place("Bernard", "B2")
salle_cinema.afficher_places_reservees()
salle_cinema.nombre_places_disponibles()
salle_cinema.filtrer_reservations_par_personne("Jonas")
salle_cinema.annuler_reservation("Bernard")
salle_cinema.reserver_place_speciale("Charlie")