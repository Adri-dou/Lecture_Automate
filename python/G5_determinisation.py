
def est_deterministe(AF: dict) -> bool:
    """Fonction qui indique si un automate est déterministe"""

    # il ne l'est pas, s'il n'a pas qu'une entrée
    if len(AF["etats_initiaux"]) != 1:
        print("L'automate n'a pas qu'une unique entrée, il n'est pas déterministe")
        return False

    # un état ne doit pas non plus engendrer plus d'une transition par la même lettre
    for etat in AF["etats"]:
        for lettre in AF["etats"][etat]:
            if len(AF["etats"][etat][lettre]) > 1:
                print(f"L'automate n'est pas déterministe, l'état {etat} "
                      f"mène vers les états {AF['etats'][etat][lettre]} depuis la lettre {lettre}")
                return False

    # si les tests on été passés, l'automate est déterministe
    return True


def determinisation(AF: dict) -> dict:
    """Renvoie un automate déterministe à partir de l'automate en paramètre"""

    

    AFD = {
        "nb_symboles": AF["nb_symboles"],
        "nb_etats": 1,
        "nb_etats_initiaux": 1,
        "etats_initiaux": [".".join(AF["etats_initiaux"])],
        "nb_etats_terminaux": 0,  # on remplira ce champ plus tard
        "etats_terminaux": [],  # pareil ici
        "nb_transitions": 0,  # idem
        "etats": {},
    }

    nouveaux_etats = [".".join(AF["etats_initiaux"])]

    while len(nouveaux_etats) > 0:
        nouvel_etat_AFD = nouveaux_etats.pop(0)

        AFD["etats"][nouvel_etat_AFD] = {}

        # on parcourt tout l'alphabet de l'automate
        for i in range(AF["nb_symboles"]):
            lettre = chr(97 + i)

            nouvel_etat_destination = []
            # on retrouve les anciens états d'origine du nouvel état
            for etat in nouvel_etat_AFD.split("."):

                # si au moins un des états d'otrigine était une sortie, celui-ci sera une sortie
                if etat in AF["etats_terminaux"] and nouvel_etat_AFD not in AFD["etats_terminaux"]:
                    AFD["etats_terminaux"].append(nouvel_etat_AFD)
                    AFD["nb_etats_terminaux"] += 1

                if lettre in AF["etats"][etat]:
                    for arrivee in AF["etats"][etat][lettre]:
                        if arrivee not in nouvel_etat_destination:
                            nouvel_etat_destination += arrivee

            if nouvel_etat_destination != []:
                nouvel_etat_destination.sort()
                AFD["etats"][nouvel_etat_AFD][lettre] = [".".join(nouvel_etat_destination)]
                nouveaux_etats.append(".".join(nouvel_etat_destination))
                AFD["nb_transitions"] += 1

        # on nettoie la liste pour être sûr qu'il ne reste que des nouveaux états
        i = 0
        while i < len(nouveaux_etats):
            if nouveaux_etats[i] in AFD["etats"]:
                del nouveaux_etats[i]
            else:
                i += 1

    return AFD
