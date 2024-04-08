
import G5_ui as ui
import G5_affichage_sauvegarde as show


TAILLE_CASE = 5  # Constante qui va définir la largeur des cases du tableau d'affichage


if __name__ == '__main__':

    # Petite séquence de tests
    mon_automate = ui.demande_utilisateur()
    show.afficher_automate(mon_automate, TAILLE_CASE)

