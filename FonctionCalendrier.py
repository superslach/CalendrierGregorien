def SommeMois(mois):  # Retourne la somme à ajouter par rapport au mois
    if mois == 1 or mois == 10:
        return 0
    elif mois == 5:
        return 1
    elif mois == 8:
        return 2
    elif mois == 2 or mois == 3 or mois == 11:
        return 3
    elif mois == 6:
        return 4
    elif mois == 9 or mois == 12:
        return 5
    elif mois == 4 or mois == 7:
        return 6

def SommeSiecle(annee):  # Retourne la somme à ajouter par rapport au siècle
    if 1581 < annee < 1600 or 1899 < annee < 2000:
        return 0
    elif 1799 < annee < 1900:
        return 2
    elif 1699 < annee < 1800 or 2099 < annee < 2200:
        return 4
    elif 1599 < annee < 1700 or 1999 < annee < 2100:
        return 6

def Bissextile(annee):  # Vérifie si l'année est bissextile ou non
    bissextile = False
    if annee % 400 == 0:    # Si l'année est divisible par 400
        bissextile = True
    elif annee % 100 == 0:  # Si l'année est divisible par 100
        bissextile = False
    elif annee % 4 == 0:    # Si l'année est divisible par 4
        bissextile = True
    return bissextile

def JourDeLaSemaine(jour):  # Récupère un jour dans la liste par rapport à son numéro
    liste = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]
    return liste[jour]

def MoisLong(mois):  # Regarde si le mois à 31 jours ou non
    if mois == 1 or mois == 3 or mois == 5 or mois == 7 or mois == 8 or mois == 10 or mois == 12:
        return True

def MoisCourt(mois):  # Regarde si le mois à 30 jours ou non
    if mois == 4 or mois == 6 or mois == 9 or mois == 11:
        return True

def MoisFevrier(mois):  # Regarde s'il s'agit du mois de Février ou non
    if mois == 2:
        return True

def MoisEnString(mois):  # Récupère un mois dans la liste par rapport à son numéro
    mois -= 1
    liste = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre",
             "Novembre", "Décembre"]
    return liste[mois]

def UpdateAnnee(annee):  # Récupère les 2 derniers chiffres dans une année donnée
    return int(annee[-2:])
