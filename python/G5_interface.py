import G5_ui as ui
import G5_affichage_sauvegarde as show
import G5_standardisation as stdrd
import G5_completion as comp
import G5_reconnaissance as reco
import G5_determinisation as deter


def main():
    while True:
        choix = input("Quel automate souhaitez-vous charger ? (Entrez 'q' pour quitter) ")
        if choix.lower() == 'q':
            print("Au revoir !\n")
            break

        try:
            automate = ui.demande_utilisateur(choix)
            show.sauvegarde_csv(automate)
            while True :
                show.afficher_automate(automate)
                print("\n\tInformation :"
                      "\nStandardisé :",stdrd.est_standard(automate),
                      "\nDeterminisé : ", deter.est_deterministe(automate),
                      "\nComplet :", comp.est_complet(automate), "\n")
                
                # Demander à l'utilisateur quelle action il souhaite effectuer
                action = input("Que voulez-vous faire ? (s = standardiser, c = vérifier la complétude, r = reconnaissance de mot, q = quitter) ").lower()
                
                if action == 's':
                    if not stdrd.est_standard(automate):
                        automate = stdrd.standardisation(automate)
                        print("L'automate a été standardisé.")
                        show.sauvegarde_csv(automate)
                    else:
                        print("L'automate est déjà standard.")
                        
                elif action == 'c':
                    if not comp.est_complet(automate):
                        automate = comp.completer_transitions_manquantes(automate)
                        print("L'automate a été complété.")
                        show.sauvegarde_csv(automate)
                    else:
                        print("L'automate est déjà complet.")
                
                elif action == 'd':
                    if not deter.est_deterministe(automate):
                        automate = deter.determinisation(automate)
                        print("L'automate a été determiniser.")
                        show.sauvegarde_csv(automate)
                    else:
                        print("L'automate est déjà determiniser")
                        
                elif action == 'r':
                    while True:
                        mot = reco.lire_mot()  # Récupérer un mot de l'utilisateur
                        if mot == "fin":
                            break  # Arrêter si l'utilisateur entre "fin"
                        resultat = reco.reconnaitre_mot(mot, automate)  
                        print("Le mot", mot, "appartient-il au langage de l'automate ? :", resultat)
                
                    
                elif action == 'q':
                    print("Au revoir !\n")
                    break
                    
                else:
                    print("Action non reconnue. Veuillez entrer 's', 'c', 'r' ou 'q'.\n")
                    
        except FileNotFoundError:
            print("Fichier non trouvé. Veuillez entrer un numéro d'automate valide.\n")

if __name__ == "__main__":
    main()
