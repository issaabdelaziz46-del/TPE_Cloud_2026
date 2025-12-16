# EXERCICE NUMERO 1 : REVERSIBILITE DE NOMBRES

# Définition d'une fonction qui prend en entrée une liste de nombres
def palindromes_numeriques(liste):
    palindromes = []  # Création d'une liste vide pour stocker les nombres palindromes
    for nombre in liste:  # Boucle sur chaque nombre de la liste
        texte = str(nombre)  # Transformation du nombre en chaîne de caractères
        if texte == texte[::-1]:  # Vérifie si le texte est identique à son inverse
            palindromes.append(nombre)  # Si oui, ajoute le nombre à la liste des palindromes
    return palindromes  # Retourne la liste des nombres palindromes trouvés


# Programme principal
entree = input("Entrez des nombres séparés par des espaces : ")
# L'utilisateur saisit des nombres séparés par des espaces

liste_nombres = list(map(int, entree.split()))
# On sépare la chaîne entrée en plusieurs éléments (split())
# Puis on convertit chaque élément en entier (int)
# Enfin on les met dans une liste

resultat = palindromes_numeriques(liste_nombres)
# On appelle la fonction pour obtenir la liste des nombres palindromes

if resultat:  # Si la liste n'est pas vide
    print("Nombres palindromes :", resultat)  # Affiche les nombres palindromes
else:  
    print("Aucun nombre palindrome trouvé.")  # Un message indique qu'aucun palindrome