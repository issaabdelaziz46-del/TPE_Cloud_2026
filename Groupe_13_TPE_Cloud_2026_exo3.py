# EXERCICE 3 : CONVERTISSEUR DE DATE

#  Vérifie si une année est bissextile
def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

# Vérifie si une date (année, mois, jour) est valide
def date_valide(annee, mois, jour):
    if mois < 1 or mois > 12:  # Mois doit être entre 1 et 12
        return False

    # Jours par mois, février dépend de l'année bissextile
    jours_par_mois = [31, 29 if est_bissextile(annee) else 28, 31, 30, 31, 30,
                      31, 31, 30, 31, 30, 31]

    if jour < 1 or jour > jours_par_mois[mois - 1]:  # Jour doit être correct
        return False

    return True

# Convertit une date AAAA-MM-JJ en JJ/MM/AAAA si elle est valide
def convertir_date(date_str):
    try:
        parts = date_str.split('-')  # Sépare la date en année, mois, jour
        if len(parts) != 3:
            return None  # Si le format est incorrect
        annee = int(parts[0])
        mois = int(parts[1])
        jour = int(parts[2])

        if date_valide(annee, mois, jour):  # Vérifie la validité de la date
            return f"{jour:02d}/{mois:02d}/{annee}"  # Retourne format JJ/MM/AAAA
        else:
            return None
    except ValueError:
        return None  # Si la conversion en entier échoue

# Programme principal

print("= EXERCICE 3 : CONVERTISSEUR DE DATE =")
date_input = input("Entrez une date au format AAAA-MM-JJ : ")
resultat = convertir_date(date_input)

if resultat:
    print("La date au format JJ/MM/AAAA est :", resultat)
else:
    print("Date invalide ! Veuillez entrer une date correcte.")
