import G5_ui as ui
import G5_affichage_sauvegarde as show
import G5_standardisation as stdrd
import G5_completion as comp
TAILLE_CASE = 5  # Constante qui va définir la largeur des cases du tableau d'affichage

def main():
    while True:
        choix = input("Quel automate souhaitez-vous charger ? (Entrez 'q' pour quitter) ")
        if choix.lower() == 'q':
            print("Au revoir !\n")
            break

        try:
            automate = ui.demande_utilisateur(choix)
            show.afficher_automate(automate, TAILLE_CASE)
            show.sauvegarde_csv(automate)
            
            if not stdrd.est_standard(automate):
                if input("L'automate n'est pas standard. Voulez-vous le standardiser ? (o/n) ").lower() == 'o':
                    automate = stdrd.standardisation(automate)
                    show.afficher_automate(automate, TAILLE_CASE)
                    show.sauvegarde_csv(automate)
            else:
                print("L'automate est standard.")


            if not comp.est_complet(automate):
                if input("L'automate n'est pas complet. Voulez-vous le compléter ? (o/n) ").lower() == 'o':
                    automate = comp.completer_transitions_manquantes(automate)
                    show.afficher_automate(automate, TAILLE_CASE)
                    show.sauvegarde_csv(automate)
            else:
                print("L'automate est compplet.")

        except FileNotFoundError:
            print("Fichier non trouvé. Veuillez entrer un numéro d'automate valide.\n")

infini = 1
if __name__ == "__main__":
    while infini < 6:
        main()
        infini+= 1
