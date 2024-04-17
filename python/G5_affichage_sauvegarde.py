import csv


def afficher_automate(automate: dict, CASE: int) -> None:
    """
    Affiche les informations d'un automate dans la console.
    """

    # Pour la première ligne, on affiche l'alphabet uniquement
    print(12*" ", end='')
    for lettre in range(0, automate["nb_symboles"]):

        # pour avoir la lettre, on part du code ASCII 97 (le a minuscule)
        print(f"{chr(97 + lettre):^{CASE}}", end='|')

    print("")

    # ici suivent les prochaines lignes en fonction des états
    for etat in automate["etats"]:

        # on affiche si l'état est initial, terminal ou aucun des deux
        if etat in automate["etats_initiaux"] and etat in automate["etats_terminaux"]:
            print(2*" " + "E S", end="|")
        elif etat in automate["etats_initiaux"]:
            print(4*" " + "E", end="|")
        elif etat in automate["etats_terminaux"]:
            print(4*" " + "S", end="|")
        else:
            print(5*" ", end="|")

        # on affiche ensuite l'état en lui-même
        print(f"{etat:^5}", end="|")

        # on va maintenant afficher les transitions en fonction de l'alphabet
        for lettre in range(0, automate["nb_symboles"]):

            if chr(97+lettre) in automate["etats"][etat]:  # on affiche les états destination de la transition
                print(f"{",".join(nb for nb in automate["etats"][etat][chr(97+lettre)]):^{CASE}}", end="|")

            else:
                print(f"{"-":^{CASE}}", end="|")

        print("")


def sauvegarde_csv(automate: dict) -> None:
    """
    Cette fonction sauvegarde l'automate dans un fichier au format csv
    """
    # on reprend le même principe que la fonction au-dessus mais pour enregistrer au lieu d'afficher
    with open("automate_sauvegarde.csv", "w", newline="") as fichier_csv:
        ecriture = csv.writer(fichier_csv, delimiter=";")

        nouvelle_ligne = 2*[""]

        # Pour la première ligne, on met l'alphabet uniquement
        for lettre in range(0, automate["nb_symboles"]):
            # pour avoir la lettre, on part du code ASCII 97 (le a minuscule)
            nouvelle_ligne.append(chr(97 + lettre))

        # on ajoute la nouvelle ligne au fichier CSV
        ecriture.writerow(nouvelle_ligne)

        # ici suivent les prochaines lignes en fonction des états
        for etat in automate["etats"]:

            # on recommence une nouvelle ligne avec si l'état est initial, terminal ou aucun des deux
            if etat in automate["etats_initiaux"] and etat in automate["etats_terminaux"]:
                nouvelle_ligne = ["E S"]
            elif etat in automate["etats_initiaux"]:
                nouvelle_ligne = ["E"]
            elif etat in automate["etats_terminaux"]:
                nouvelle_ligne = ["S"]
            else:
                nouvelle_ligne = [""]

            # on ajoute ensuite l'état en lui-même
            nouvelle_ligne.append(etat)

            # on va maintenant afficher les transitions en fonction de l'alphabet
            for lettre in range(0, automate["nb_symboles"]):

                if chr(97 + lettre) in automate["etats"][etat]:
                    nouvelle_ligne.append(",".join(nb for nb in automate["etats"][etat][chr(97 + lettre)]))

                else:
                    nouvelle_ligne.append("-")

            ecriture.writerow(nouvelle_ligne)
