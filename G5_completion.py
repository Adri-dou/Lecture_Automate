
def est_complet(AF: dict) -> bool:
    """
    Cette fonction renvoie un booléen disant si l'automate en paramètre est complet ou non
    """
    # un automate est non complet si dans ça table de transition il y a des trou ici representé par "-".
    with open("./automate_sauvegarde.csv", "r") as f:
        lignes = f.readlines()
        for ligne in lignes:
            if '-' in ligne:
                return False

        # ici le caractère '-' n'a pas été trouvé dans les ligne
        return True


def trouver_manquants(AF: dict) -> list:
    """
    Cette fonction renvoie une liste de tuples contenant les endroits où
    il manque une transition pour tous les symboles de l'alphabet dans l'automate.
    Chaque tuple contient l'état et le symbole pour lequel il manque une transition.
    """

    manquants = []
    etats = AF['etats']

    # on récupère tous les symboles de l'alphabet
    alphabet = set()
    for transitions_etat in etats.values():
        alphabet.update(transitions_etat.keys())

    # parcourir tous les états de l'automate et vérifier s'il manque une transition pour chaque symbole de l'alphabet
    for etat, transitions_etat in etats.items():
        for symbole in alphabet:
            if symbole not in transitions_etat:
                manquants.append((etat, symbole))  # Ajouter l'endroit où il manque une transition à la liste

    return manquants


def completer_transitions_manquantes(AF: dict) -> dict:
    """
    Cette fonction complète les transitions manquantes dans l'automate en ajoutant un état poubelle 'P'
    avec des transitions vers lui-même pour chaque symbole de l'alphabet.
    """
    etats = AF['etats']  # Récupérer les états de l'automate
    alphabet = set()  # Créer un ensemble pour stocker les symboles de l'alphabet
    transitions_manquantes = trouver_manquants(AF)  # Trouver les transitions manquantes

    # Récupérer tous les symboles de l'alphabet
    for transitions_etat in etats.values():
        alphabet.update(transitions_etat.keys())

    # Ajouter l'état poubelle 'P' à l'automate s'il n'existe pas déjà
    if 'P' not in etats:
        etats['P'] = {symbole: ['P'] for symbole in alphabet}

    # Ajouter des transitions depuis l'état poubelle 'P' vers lui-même pour chaque symbole de l'alphabet
    for symbole in alphabet:
        etats['P'][symbole] = ['P']

    # Ajouter des transitions manquantes vers l'état poubelle 'P' dans l'automate
    for etat, symbole in transitions_manquantes:
        etats[etat][symbole] = ['P']

    return AF
