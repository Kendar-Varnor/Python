# Importation du module de nombre aléatoire.
import random

# Boucle de jeu.
partie = "o"

while partie == "o":

    # Initialisation des variables.
    nombre_cpu = random.randint(1, 100)
    essai = 5

    # Explication des règles du jeu.
    print("--------------------------------------------------------------------------------")
    print("")
    print("Marteaux et clou")
    print("")
    print("Règles du jeu :")
    print("Je pense à un nombre compris entre 1 et 100. Votre but est de le deviner en")
    print(str(essai) + " essais.")
    print("")

    # Phase de jeu.
    while essai >= 0:
        
        # Entrer le nombre à deviner.
        print("Quel est le nombre auquel je pense ?")
        nombre = int(input())
        print("")


        # Mécanique de jeu.
        if nombre > nombre_cpu:
            print("Votre nombre est trop élevé.")
            essai -= 1
            print("Il vous reste " + str(essai) + " essai(s).")
            print("")
        elif nombre < nombre_cpu:
            print("Votre nombre est trop bas.")
            essai -= 1
            print("Il vous reste " + str(essai) + " essai(s).")
            print("")
        elif nombre == nombre_cpu:
            print("Félicitations ! Vous avez trouvé le bon nombre.")
            print("C'était " + str(nombre_cpu) + " !")
            print("")
            break
        else:
            print("Veuillez entrer un nombre compris entre 1 et 100 s\'il-vous-plaît")
            print("")

        if essai == 0:
            print("Vous avez perdu.")
            print("")
            break

    # Demande de nouvelle partie.
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
