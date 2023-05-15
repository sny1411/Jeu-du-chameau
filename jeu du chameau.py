from random import randint

KM_VOYAGE = 300         # Distance à parcourir pour gagner.
KM_NORM_MIN = 10        # Distance min. à la vitesse normale.
KM_NORM_MAX = 15        # Distance max. à la vitesse normale.
KM_RAP_MIN = 20         # Distance min. à toute vitesse.
KM_RAP_MAX = 25         # Distance max. à toute vitesse.
AVANTAGE_VOYAGEUR = 20  # L'avantage initiale du voyageur.
GOURDE_PLEINE = 12      # Le nombre de gorgées de la gourde.
MORT_SOIF = 4           # Nombre de tours pour mourir de soif.
MORT_FATIGUE = 4        # Nombre de tours pour mourir de fatigue.
DIF_AIDE = 3            # Difficulté pour trouver de l'aide.
AVANCE_NATIFS = 8       # Vitesse des natifs.
SPECIAL = 30
KM_MIN_ADD = 25
KM_MAX_ADD = 100

jeuLancer = True
while jeuLancer:
    km_fin = KM_VOYAGE + randint(KM_MIN_ADD,KM_MAX_ADD)
    print("LE JEU DU CHAMEAU")
    print("Vous avez volé un chameau pour traverser le grand désert.")
    print("Les natifs veulent le récuperer.")
    print("Votre objectif est de survivre à la traverée de",km_fin,"km sans être attrapé(e).")

    km_voyageur = 0                             # Distance totale parcourue.
    km_natifs = km_voyageur - AVANTAGE_VOYAGEUR # Distance parcourue par les natifs
    gourde = GOURDE_PLEINE // 2                 # Nombre de gorgés dans la gourde.
    soif = 0                                    # Niveau de soif du voyageur.
    fatige = 0                                  # Niveau de fatigue du chameau.
    

    continuer = True
    while continuer:
        special = randint(0,SPECIAL)
        if special == 0: # oasis
            optionValide = False
            while not optionValide:
                print("Vous avez trouvez une oasis !")
                print("\nOPTIONS :")
                print("1. Remplir la gourde")
                print("2. Ne rien faire")
                print("T. Terminer la partie")
                choix = input("\nQu'allez-vous faire ? ")
                optionValide = choix == "1" or choix == "2" or choix == "T"
                if not optionValide:
                    print("Option invalide !")

                if choix == "1":
                    gourde = GOURDE_PLEINE
                    print("Votre gourde est désormais pleine !\n")
                elif choix == "2":
                    print("vous ne vous arretez pas.")
                elif choix == "T":
                    continuer = False
        elif special == 1: # tempête
            print("Une tempête s'abat sur le désert !")
            print("Vous ne pouvez rien faire.\n")
            distanceAlea = randint(KM_NORM_MIN,KM_NORM_MAX)
            km_natifs += distanceAlea
        else:
            optionValide = False
            while not optionValide:
                print("\nOPTIONS :")
                print("1. Boire")
                print("2. Avancer normalement")
                print("3. Avancer à toute vitesse")
                print("4. Repos")
                print("5. Espérer de l'aide")
                print("T. Terminer la partie")
                choix = input("\nQu'allez-vous faire ? ")
                optionValide = choix == "1" or choix =="2" or choix == "3" or choix == "4" or choix == "5" or choix == "T"
                if not optionValide:
                    print("Option invalide !")

            if choix == "1":
                if gourde == 0:
                    print("La gourde est vide !")
                else:
                    gourde -= 1
                    soif = 0
                    print("Vous avez bu une gorgée.")
            elif choix == "2":
                fatige += 1
                distanceAlea = randint(KM_NORM_MIN,KM_NORM_MAX)
                km_voyageur += distanceAlea
                print("Vous avez avancé de",distanceAlea,"km.")
            elif choix == "3":
                fatige += 2
                distanceAlea = randint(KM_RAP_MIN,KM_RAP_MAX)
                km_voyageur += distanceAlea
                print("Vous avez avancé rapidement de",distanceAlea,"km.")
            elif choix == "4":
                fatige = 0
                print("Votre chameau s'est bien reposé.")
            elif choix == "5":
                nbreAlea = randint(0,DIF_AIDE)
                if nbreAlea == 0:
                    print("Vous avez trouvé de l'aide.")
                    if gourde >= GOURDE_PLEINE:
                        print("La gourde est déjà pleine!")
                    else:
                        if (gourde + 3) >= 6:
                            gourde = GOURDE_PLEINE
                        else:
                            gourde += 3
                        print("Quelques gorgées ont été ajoutées à votre gourde.") 
                else:
                    print("Vous n'avez pas trouvé de l'aide.")
            elif choix == "T":
                continuer = False

            soif += 1 # Soif

            avancementNatif = randint(0,AVANCE_NATIFS) # avancement des natifs
            if avancementNatif == 0:
                distanceAlea = randint(KM_RAP_MIN - 5,KM_RAP_MAX - 5)
                km_natifs += distanceAlea
            else:
                distanceAlea = randint(KM_NORM_MIN - 1,KM_NORM_MAX - 1)
                km_natifs += distanceAlea       

        # test fin partie
        if km_voyageur >= km_fin:
            print("Vous avez gagné")
            continuer = False
        elif km_natifs >= km_voyageur:
            print("Vous avez été attrapé par les natifs ! ")
            continuer = False
        elif soif > MORT_SOIF:
            print("Le voyageur est mort de soif.")
            continuer = False
        elif fatige > MORT_FATIGUE:
            print("Votre chameau est mort de fatigue. \nLe voyageur à été attrapé par les natifs.")
            continuer = False
        else:
            print("\nVous avez parcouru un total de",km_voyageur,"km jusqu'ici. (sur ",km_fin,")")
            print("Vous avez",km_voyageur-km_natifs, "km d'avance sur les natifs.")
            if soif == 0:
                print("Vous n'avez pas soif.")
            elif soif == 1:
                print("Vous avez un peu soif.")
            elif soif == 2:
                print("Vous avez beacoup soif !")
            elif soif > 2:
                print("Vous allez mourir de soif !!")
            print("Votre gourde contient", gourde, "gorgées d'eau.") # gourde
            if fatige == 0:
                print("Le chameau est en bonne forme.")
            elif fatige == 1:
                print("Le chameau est un peu fatigué.")
            elif fatige == 2:
                print("Le chameau est très fatigué !")
            elif fatige > 2:
                print("Le chameau va mourir de fatigue !!")

    choixRejouer = ""
    while choixRejouer != "o" and choixRejouer != "n":
        choixRejouer = input("Voulez-vous jouer une nouvelle partie ? (o / n) ")
    jeuLancer = choixRejouer == "o"

