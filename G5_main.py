
import G5_ui as ui
import G5_affichage_sauvegarde as show

TAILLE_CASE = 5

if __name__ == '__main__':
    mon_automate = ui.demande_utilisateur()
    show.afficher_automate(mon_automate, TAILLE_CASE)

