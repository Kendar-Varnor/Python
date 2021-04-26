# Importation du module random pour générer des nombres aléatoires.
import random

# Boucle de jeu.
partie = "o"

while partie == "o":

    # Initialisation des variables.
    pv_clou = 100
    joueur = ""
    cpu = "Orlane"
    puissance_joueur = 0
    puissance_cpu = 0
    phase_jeu = 1

    # Explication des règles de marteaux et clou.
    print("--------------------------------------------------------------------------------")
    print("")
    print("Marteaux et clou")
    print("")
    print("Règles du jeu :")
    print("Vous allez jouer contre " + cpu + " à un jeu particulier. Un clou est planté sur la")
    print("table. Chacun votre tour, vous allez frapper sur le clou avec votre marteau et")
    print("vous allez mettre dans ce coup la puissance que vous désirez. Le ou la dernière")
    print("à enfoncer complètement le clou sur la table gagne la partie.")
    print("")
    print("La durée du jeu est symbolisé par les points de vie du clou, qui en possède" + str(pv_clou))
    print("au départ. On considère qu'à 0 points de vie, ce clou est complètement enfoncé")
    print("sur la table.")
    print("")

    # Entrer le nom du joueur.
    print("Joueur ou joueuse, entrez votre nom :")
    joueur = str(input())
    print("")

    # Fonction de frappe de marteau sur le clou.
    def coup_marteau(personnage, puissance):
        global pv_clou
        degats = random.randint(1, 4) + puissance
        pv_clou -= degats

        print(personnage + " inflige " + str(degats) + " dégâts au clou avec son marteau.")
        print("Le clou n'a plus que " + str(pv_clou) + " points de vie.")
        print("")

    # Fonction du tour du joueur.
    def tour_de_joueur():
        global joueur
        global puissance_joueur

        choix_puissance = 0
        
        print(joueur + ", entrez la puissance de votre coup de marteau entre 1 et 6 :")
        print("1 = Puissance très faible")
        print("2 = Puissance faible")
        print("3 = Puissance moyenne")
        print("4 = Puissance forte")
        print("5 = Puissance très forte")
        print("6 = Puissance max")
        print("")
        
        while choix_puissance == 0:
            print("Votre puissance :")
            puissance_joueur = int(input())
            print("")

            if puissance_joueur < 1 or puissance_joueur > 6:
                print("Veuillez entrer une puissance comprise entre 1 et 6 s\'il-vous-plaît.")
            else:
                choix_puissance = 1
                break
                               
        coup_marteau(joueur, puissance_joueur)

    # Fonction du tour du cpu.
    def tour_de_cpu():
        
        global puissance_cpu
        
        puissance_cpu = random.randint(1, 6)
        
        coup_marteau(cpu, puissance_cpu)

    # Phase de jeu.
    while phase_jeu == 1:
        tour_de_joueur()
        if pv_clou <= 0:
            print ("Vous avez gagné. Félicitations !")
            print("")
            print("--------------------------------------------------------------------------------")
            phase_jeu == 0
            break
        
        tour_de_cpu()
        if pv_clou <= 0:
            print ("Vous avez perdu. Dommage !")
            print("")
            print("--------------------------------------------------------------------------------")
            phase_jeu == 0
            break

    # Demande de nouvelle partie ou non.
    partie = "n"
    print("Voulez-vous jouer une nouvelle partie ?")
    print("Tapez \"o\" pour jouer une nouvelle partie, \"n\" pour arrêter de jouer.")
    print("")
    print("Votre réponse :")
    partie = input()
    if partie == "n":
        print("--------------------------------------------------------------------------------")
        print("")
        print("Game Over")
        print("")
        print("--------------------------------------------------------------------------------")
        break

