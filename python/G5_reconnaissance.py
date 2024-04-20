
def est_reconnu(langage: str, automate: dict) -> bool:
    """
    Fonction qui vérifie si le langage donné est reconnu par l'automate spécifié.
    """
    if not langage:  # pour le mot vide, vérif si un état initial est également un état terminal
        return any(etat in automate['etats_terminaux'] for etat in automate['etats_initiaux'])

    etats_actuels = automate['etats_initiaux']
    etats_terminaux = set(automate['etats_terminaux'])

    for lettre in langage:
        etats_suivants = set()

        # Pour chaque état actuel, on regarde les états suivants après avoir consommé la lettre actuelle
        for etat in etats_actuels:
            transitions_etat = automate['etats'].get(etat, {})  # transitions possibles pour l'état actuel
            etats_suivants.update(transitions_etat.get(lettre, []))  # ajoutons les états suivants pour cette lettre

        # on met à jour
        etats_actuels = etats_suivants

    # après avoir parcouru tous les symboles du langage, vérifions si nous avons atteint un état terminal
    return bool(etats_actuels & etats_terminaux)


def lire_mot() -> str:
    """
    Fonction pour récupérer un mot donné par l'utilisateur au clavier.
    """
    mot = input("Entrez un mot (ou 'fin' pour arrêter) : ")
    return mot


def reconnaitre_mot(mot: str, automate: dict) -> str:
    """
    Fonction pour reconnaître si un mot donné appartient ou non au langage spécifié par l'automate.
    """
    if est_reconnu(mot, automate):
        return "oui"
    else:
        return "non"



