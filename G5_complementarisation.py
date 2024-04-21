def complementarisation(AFDC: dict, minimal: bool = False) -> dict:
    """
    Fonction qui renvoie l'automate complémentaire de l'automate donné
    """

    AComp = AFDC.copy()

    # pour trouver l'automate complémentaire on inverse les sorties
    anciens_terminaux = AFDC["etats_terminaux"].copy()

    # on vide la liste
    AComp["etats_terminaux"].clear()
    for etat in AComp["etats"]:
        if etat not in anciens_terminaux:
            AComp["etats_terminaux"].append(etat)

    if minimal:
        print("\nAutomate complémentaire depuis un automate déterministe complet minimal")
    else:
        print("\nAutomate complémentaire depuis un automate déterministe complet")

    return AComp
