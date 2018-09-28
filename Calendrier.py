from FonctionCalendrier import *  # Import de toutes les fonctions
verification = False

while verification == False :
    date = input("Saisir une date sous la forme JJ/MM/AAAA ou JJ-MM-AAAA (Date française) : ")  # saisie de la date sous la forme JJ/MM/AAAA
    if date.__contains__("/"):
        jour, mois, annee = date.split("/")  # séparation de la date en 3 valeurs
    elif date.__contains__("-"):
        jour, mois, annee = date.split("-")  # séparation de la date en 3 valeurs
    if jour == '' or mois == '' or annee == '':
        print("Le format n'est pas respecté")
    else:
        jour = int(jour)
        mois = int(mois)
        annee = int(annee)
        if date.count("/", 0, 9) == 2 or date.count("-", 0, 9) == 2:  # Si la date est au bon format
            if MoisCourt(mois) and 0 < jour < 31 \
                    or MoisLong(mois) and 0 < jour < 32 \
                    or Bissextile(annee) and MoisFevrier(mois) and 0 < jour < 30 \
                    or Bissextile(annee) is False and MoisFevrier(mois) and 0 < jour < 29:  # On cherche à définir le nombre de jours dans le mois inséré
                verification = True
            else:
                print("Cette date n'existe pas")
        else:
            print("Ce n'est pas le bon format")

if annee <= 1582 and mois < 11:  # On regarde si la date est inférieure au 1er Novembre 1582
    print("La date que vous avez entré correspond au ", jour, "", MoisEnString(mois), "", annee, ". Cette méthode ne permet pas de calculer des dates inférieures au 1er Novembre 1582")

else:
    somme = UpdateAnnee(str(annee))  # On récupère les 2 derniers chiffres de l'année
    somme += somme // 4  # On ajoute 1/4 de ce nombre en ignorant les restes
    somme += jour      # On ajoute la valeur du jour dans le mois à la somme
    somme += SommeMois(mois)    # Utilisation de la fonction SommeMois() et ajout de la valeur

    if Bissextile(annee) and mois <= 2:  # On cherche à savoir si l'année est bissextile et si le mois est Janvier ou Février
        somme -= 1
    somme += SommeSiecle(annee)     # Utilisation de la fonction SommeSiecle() et ajout de la valeur
    reste = somme % 7    # Modulo du total des sommes

    jourSemaine = JourDeLaSemaine(reste)   # Utilisation de la fonction JourDeLaSemaine()
    print("Le jour de la semaine correspondant est : ", jourSemaine)
