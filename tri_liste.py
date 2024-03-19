def tri_croissant(liste):
    return sorted(liste)

liste_de_nombres = [15, 12, 18, 11, 13]
liste_triee = tri_croissant(liste_de_nombres)
print(f"Liste initiale : {liste_de_nombres}")
print(f"Liste triée par ordre croissant : {liste_triee}")