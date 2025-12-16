# EXERCICE 5 : COMPRESSION DE TEXTE

def compression_texte(texte):
    """
    Compresse un texte en remplaçant les lettres répétées par un compteur.
    """
    if not texte:
        return ""  # Si la chaîne est vide, on retourne une chaîne vide

    resultat = ""          # Chaîne compressée
    compteur = 1           # Compteur pour les lettres répétées
    precedent = texte[0]   # Première lettre à comparer

    # Parcourir le texte à partir du deuxième caractère
    for caractere in texte[1:]:
        if caractere == precedent:
            compteur += 1
        else:
            # Ajouter la lettre précédente et son compteur
            resultat += precedent + str(compteur)
            precedent = caractere
            compteur = 1

    # Ajouter le dernier caractère et son compteur
    resultat += precedent + str(compteur)

    return resultat


# PROGRAMME PRINCIPAL ----------------------

print("= EXERCICE 5 : COMPRESSION DE TEXTE =")

texte_input = input("Entrez une chaîne de caractères à compresser : ")

texte_compresse = compression_texte(texte_input)

print("Texte compressé :", texte_compresse)
