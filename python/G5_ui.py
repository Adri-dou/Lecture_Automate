

def demande_utilisateur() -> dict:
    """
    Lit l'automate que l'utilisateur souhaite à partir d'un fichier texte
    et renvoie un dictionnaire représentant l'automate.
    """

    user_input = input("Quel automate souhaitez-vous charger ?")
    if len(user_input) < 2:
        user_input = "0" + user_input

    # on ouvre le fichier en lecture
    with open(f"./automates/G5-{user_input}.txt", "r") as f:
        lignes = f.readlines()

    # Création du dictionnaire de l'automate
    nouvel_automate = {
        "nb_symboles": int(lignes[0]),
        "nb_etats": int(lignes[1]),
        "nb_etats_initiaux": int(lignes[2][0]),
        "etats_initiaux": [etat[0] for etat in lignes[2].split(" ")][1:],
        "nb_etats_terminaux": int(lignes[3][0]),
        "etats_terminaux": [etat[0] for etat in lignes[3].split(" ")][1:],
        "nb_transitions": int(lignes[4][0]),
        "etats": {},
    }

    # on remplit les états
    for i in range(nouvel_automate["nb_etats"]):
        nouvel_automate["etats"][str(i)] = {}

    transitions = [ligne.strip().split(" ")[0] for ligne in lignes[5:]]
    # la fonction strip() permet de retirer les espaces en trop et le \n à la fin des lignes

    # maintenant on organise les transistions pour savoir exactement quel état mène vers quels autres états
    for transition in transitions:

        # si l'on n'a pas encore enregistré cet états
        if transition[0] not in nouvel_automate["etats"]:
            nouvel_automate["etats"][transition[0]] = {transition[1]: [transition[2]]}

        # si l'état est enregistré mais pas cette lettre de l'alphabet
        elif transition[1] not in nouvel_automate["etats"][transition[0]]:
            nouvel_automate["etats"][transition[0]][transition[1]] = [transition[2]]

        # le dernier cas est celui où on ajoute un autre état à cette transition
        else:
            nouvel_automate["etats"][transition[0]][transition[1]].append(transition[2])
            nouvel_automate["etats"][transition[0]][transition[1]].sort()  # on trie pour que ce soit plus propre à l'affichage

    print(nouvel_automate)

    return nouvel_automate


