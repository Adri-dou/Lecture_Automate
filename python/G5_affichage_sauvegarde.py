
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

            etats_suivants = ""
            if chr(97+lettre) in automate["etats"][etat]:
                print(f"{",".join(nb for nb in automate["etats"][etat][chr(97+lettre)]):^{CASE}}", end="|")

            else:
                print(f"{"-":^{CASE}}", end="|")

        print("")
