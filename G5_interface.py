
import G5_affichage_sauvegarde as show
import G5_standardisation as stdrd
import G5_completion as comp
import G5_reconnaissance as reco
import G5_determinisation as deter
import G5_complementarisation as comple


def main():
    """
    Fonction principale de notre projet, elle contient la boucle générale du programme
    """

    while True:  # première boucle infinie qui va permettre à l'utilisateur de faire son choix d'automate
        choix = input("Quel automate souhaitez-vous charger ? (Entrez 'q' pour quitter) ")
        if choix.lower() == 'q':
            print("Au revoir !\n")
            break

        # on teste si l'automate est trouvé
        try:
            # on va créer un automate en lisant le txt du choix de l'utilisateur, puis le sauvegarder
            automate = lecture_automate(choix)
            show.sauvegarde_csv(automate)

            # 2e boucle infinie pour le choix des actions
            while True:
                show.afficher_automate(automate)
                print("\n\tInformations :"
                      "\nStandard :", stdrd.est_standard(automate),
                      "\nDeterministe : ", deter.est_deterministe(automate),
                      "\nComplet :", comp.est_complet(automate), "\n")
                
                # Demander à l'utilisateur quelle action il souhaite effectuer
                action = input("\nQue voulez-vous faire ?  "
                               "(s = standardiser, d = vérifier s'il est déterministe, "
                               "c = vérifier la complétude, r = reconnaissance de mot, "
                               "k = complémentarisation q = quitter) ").lower()
                
                if action == 's':
                    if not stdrd.est_standard(automate):
                        automate = stdrd.standardisation(automate)
                        print("L'automate a été standardisé")
                        show.sauvegarde_csv(automate)
                    else:
                        print("L'automate est déjà standard")
                
                elif action == 'd':
                    if not deter.est_deterministe(automate):
                        if input("\n\tSouhaitez-vous déterminiser l'automate ? (o/n) :").lower() == 'o':
                            automate = deter.determinisation(automate)
                            print("L'automate a été determinisé")
                            show.sauvegarde_csv(automate)
                        else:
                            print("L'automate n'a pas été déterminisé")
                    else:
                        print("L'automate est déjà deterministe")

                elif action == 'c':  # pour le compléter, l'automate doit d'abord être déterministe
                    if not deter.est_deterministe(automate):
                        automate = deter.determinisation(automate)
                        print("L'automate a été determinisé pour pouvoir être complété")
                        show.sauvegarde_csv(automate)
                    if not comp.est_complet(automate):
                        manquants = comp.trouver_manquants(automate)
                        for manquant in manquants:
                            print(f"Il manque une transition pour l'état {manquant[0]} et le symbole {manquant[1]}")

                        if input("\n\tVoulez vous compléter l'automate ? (o/n) :").lower() == 'o':
                            automate = comp.completer_transitions_manquantes(automate)
                            print("L'automate a été complété")
                            show.sauvegarde_csv(automate)
                        else:
                            print("L'automate na pas été complété")

                    else:
                        print("L'automate est déjà complet")
                        
                elif action == 'r':
                    while True:
                        mot = reco.lire_mot()  # Récupérer un mot de l'utilisateur
                        if mot == "fin":
                            break  # Arrêter si l'utilisateur entre "fin"
                        resultat = reco.reconnaitre_mot(mot, automate)  
                        print("Le mot '" + mot + "' appartient-il au langage de l'automate ? :", resultat)

                elif action == 'k':  # un automate doit être au moins déterministe et complet
                    if deter.est_deterministe(automate) and comp.est_complet(automate):
                        comple.complementarisation(automate)
                    
                elif action == 'q':
                    print("Vous pouvez choisir un autre automate...\n")
                    break
                    
                else:
                    print("Action non reconnue. Veuillez entrer 's', 'd', 'c', 'r' ou 'q'.\n")

        # si l'automate n'est pas trouvé on le fait remarquer à l'utilisateur, il pourra refaire un choix
        except FileNotFoundError:
            print("Fichier non trouvé. Veuillez entrer un numéro d'automate valide.\n")


def lecture_automate(choix: str) -> dict:
    """
    Lit l'automate que l'utilisateur souhaite à partir d'un fichier texte
    et renvoie un dictionnaire représentant l'automate.
    """
    user_input = choix

    if len(user_input) < 2:
        user_input = "0" + user_input

    # on ouvre le fichier en lecture
    with open(f"G5-{user_input}.txt", "r") as f:
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

    #print(nouvel_automate)

    return nouvel_automate


if __name__ == "__main__":
    main()
