
def demande_utilisateur():
    """
    Lit l'automate que l'utilisateur souhaite à partir d'un fichier texte
    et renvoie un dictionnaire représentant l'automate.
    """

    user_input = int(input("Quel automate souhaitez-vous charger ?"))

    # on ouvre le fichier en lecture
    with open(f"G5-{user_input}.txt", "r") as f:
        lignes = f.readlines()

    # Création du dictionnaire de l'automate
    nouvel_automate = {
        "nb_symboles": int(lignes[0]),
        "nb_etats": int(lignes[1]),
        "nb_etats_initiaux": int(lignes[2][0]),
        "etats_initiaux": [int(x) for x in lignes[2].split(" ")][1:],
        "nb_etats_terminaux": int(lignes[3][0]),
        "etats_terminaux": [int(x) for x in lignes[3].split(" ")][1:],
        "nb_transitions": int(lignes[4][0]),
        "transitions": [ligne.strip().split(" ")[0] for ligne in lignes[5:]],
        # la fonction strip() permet de retirer les espaces en trop et le \n à la fin des lignes
    }

    return nouvel_automate


