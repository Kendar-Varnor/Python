# Importation du module random pour générer des nombres aléatoires.
import random

# Boucle de jeu.
partie = "o"

while partie == "o":
        
        # Initialisation des variables.
        blackjack = 0
        carte = 0
        nb_carte = 0

        # Explications des règles du blackjack.
        print("--------------------------------------------------------------------------------")
        print("")
        print("Blackjack")
        print("")
        print("Règles du jeu :")
        print("Vous allez tirer aléatoirement des cartes.")
        print("Chacune d'elle possède une valeur allant de 1 à 10.")
        print("Le but est d'obtenir le résultat le plus élevé, mais ne pas dépasser 21.")
        print("A chaque tirage de carte, vous êtes libre de continuer ou non.")
        print("Par la suite, on compte le total des valeurs de cartes obtenus.")
        print("")
        
        # Phase de jeu.
        while blackjack < 21:
                # Demander si le joueur veut tirer une carte ou non.
                print("Voulez-vous tirer une carte ?")
                print("Tapez \"o\" pour tirer une carte, \"n\" pour ne pas le faire.")
                print("")
                print("Votre réponse :")
                choix = input()
                print("")
                # Si oui, instructions pour tirer une carte et compter les points.
                if choix == "o":
                        carte = random.randint(1, 10)
                        print("Vous tirez une carte de valeur " + str(carte) + ".")          
                        nb_carte += 1
                        print("Vous avez tiré au total " + str(nb_carte) + " cartes.") 
                        blackjack += carte
                        print("")
                        print("Vous avez " + str(blackjack) + " points.")
                        print("")
                # Si non, fin du jeu et comptage des points.
                elif choix == "n":
                        print("")
                        print("--------------------------------------------------------------------------------")
                        print("")
                        break
                
                # Si le joueur a entré autre chose, on lui redemande s'il veut ou non tirer une carte.
                else:
                        print("Veuillez entrer \"o\" ou \"n\" s'il-vous-plait.")
                        print("")

        # Conditions de fin de jeu.
        if blackjack > 21:
                print("Vous avez perdu.")
                print("")
        if blackjack < 21 and choix == "n":
                print("Vous avez obtenu un total de " + str(blackjack) + " points.")
                print("")
        if blackjack == 21:
                print("Félicitations, vous avez obtenu 21 points !")
                print("")
                
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
