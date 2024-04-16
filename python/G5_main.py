
import G5_ui as ui
import G5_affichage_sauvegarde as show
import G5_standardisation as stdrd


TAILLE_CASE = 5  # Constante qui va définir la largeur des cases du tableau d'affichage


if __name__ == '__main__':

    # Petite séquence de tests
    mon_automate = ui.demande_utilisateur()
    show.afficher_automate(mon_automate, TAILLE_CASE)
    print(stdrd.est_standard(mon_automate))

    mon2eautomate = stdrd.standardisation(mon_automate)
    show.afficher_automate(mon2eautomate, TAILLE_CASE)
