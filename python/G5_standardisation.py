
def est_standard(AF: dict) -> bool:
    """
    Cette fonction renvoie un booléen disant si l'automate en paramètre est standard ou non
    """
    # un automate est non standard s'il n'a pas qu'une seule entrée
    if AF["nb_etats_initiaux"] != 1:
        return False

    else:
        # s'il y a une transition vers l'état d'entrée, l'automate n'est pas standard
        for etat in AF["etats"]:
            for lettre in AF["etats"][etat]:
                if AF["etats_initiaux"][0] in AF["etats"][etat][lettre]:
                    return False

    # si l'automate a passé les tests il est standard
    return True


def standardisation(AF: dict) -> dict:
    """
    Fonction qui standardise un automate s'il ne l'est pas déjà
    """
    if est_standard(AF):
        print("L'automate est déjà standard")
        return AF

    # on crée le nouvel état itinial "i"
    AF["etats"]["i"] = {}

    for entree in AF["etats_initiaux"]:
        for cle, val in AF["etats"][entree].items():
            if cle in AF["etats"]["i"]:
                AF["etats"]["i"][cle] += val
            else:
                AF["etats"]["i"][cle] = val.copy()

        # on déporte également les sorties si le mot vide doit être reconnu
        if entree in AF["etats_terminaux"] and 'i' not in AF["etats_terminaux"]:
            print("test")
            AF["etats_terminaux"].append('i')

    AF["nb_etats_initiaux"] = 1
    AF["etats_initiaux"] = ['i']

    return AF
