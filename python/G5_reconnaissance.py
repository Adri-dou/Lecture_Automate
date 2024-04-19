
def est_reconnu(langage: str, automate: dict) -> bool:
    """
    Vérifie si le langage donné est reconnu par l'automate spécifié.
    """
    if not langage:  # Si le langage est vide, vérif si un état initial est également un état terminal
        return any(etat in automate['etats_terminaux'] for etat in automate['etats_initiaux'])

    etats_actuels = automate['etats_initiaux']  # Débutons à partir des états initiaux
    etats_terminaux = set(automate['etats_terminaux'])  # Ensemble des états terminaux

    for symbole in langage:
        etats_suivants = set()  # Ensemble des états suivants après avoir consommé le symbole actuel

        # Pour chaque état actuel, on regarde les états suivants après avoir consommé le symbole actuel
        for etat in etats_actuels:
            transitions_etat = automate['etats'].get(etat, {})  # Transitions possibles pour l'état actuel
            etats_suivants.update(transitions_etat.get(symbole, []))  # Ajoutons les états suivants pour ce symbole

        etats_actuels = etats_suivants  # Mettons à jour les états actuels pour passer à l'étape suivante

    # Après avoir parcouru tous les symboles du langage, vérifions si nous avons atteint un état terminal
    return bool(etats_actuels & etats_terminaux)


def lire_mot():
    """
    Fonction pour récupérer un mot donné par l'utilisateur au clavier.
    """
    mot = input("Entrez un mot (ou 'fin' pour arrêter) : ")
    return mot


def reconnaitre_mot(mot, automate):
    """
    Fonction pour reconnaître si un mot donné appartient ou non au langage spécifié par l'automate.
    """
    if est_reconnu(mot, automate):
        return "oui"
    else:
        return "non"



