"""
Celine Mattar
403
Combat des monstres

"""

import random

def menu():
    """
    Que voulez vous faire: \n 1- le combattre  \n 2- ouvrir une autre porte \n 3- afficher les regles \n 4- quitter

    """

boucle_jeu = True
while boucle_jeu:
    adversaire = random.randint(1, 5)
    vie = 20
    print(menu)
    demarage = int(input("Choisissez un chiffre:"))

    if demarage == 1:
        jouer = random.randint(1, 6)
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
            print("le monstre vous a batu, vous perdez: " + str(adversaire))
            vie = 20 - adversaire
            print(vie)
        else:
            print("reasseyer")

    if demarage == 2:
        vie = 20 - 1
        print("Vous perdez 1 vie")
        print("Il vous reste " + str(vie) + " vie")
        print(menu)

    if demarage == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire. "
              "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.  Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire. ")
        print("La partie se termine lorsque les points de vie de l’usager tombent sous 0. "
              "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.")

    if demarage == 4:
        boucle_jeu = False










