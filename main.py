"""
Celine Mattar
403
Combat des monstres

"""

import random

def menu():


    print("Que voulez vous faire:"
                "1- le combattre "
                "2- ouvrir une autre porte "
                "3- afficher les regles "
                "4- quitter")


boucle_jeu = True
while boucle_jeu:
    adversaire = random.randint (1, 5)
    vie = 20
    #print("La force de votre adversaire est de" + str(adversaire))
    print(menu)
    demarage = int(input("Choisissez un chiffre:"))

    if demarage == 1:
        jouer = random.randint (1, 6)
        print(jouer)
        print("Force adversaire: " + str(adversaire))
        print("votre force: " + str(jouer))
        print("niveau de vie: " + str(vie))
        print("combat: " + str(jouer) + " vs " + str(adversaire))

        if jouer > adversaire:
            print("Vous avez batu le montstre, vous gagnez " + str(adversaire))
            vie = 20 + adversaire
            print(vie)
            print(menu)
        elif jouer < adversaire:
            print ("le monstre vous a batu, vous perdez: " + str(adversaire))
            vie = 20 - adversaire
            print(vie)
        else:
            print("reasseyer")








