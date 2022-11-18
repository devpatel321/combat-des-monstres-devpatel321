"""
Créé par Dev Patel du groupe 402
Créé le 29 septembre 2022
Jeu de monstres
"""

from random import randint

niveau_vie = 20
numero_combat = 0
nombre_victoires = 0
victoires_consecutives = 0
nombre_defaites = 0
numero_adversaire = 0
force_adversaire = randint(1, 5) + randint(1, 5)
nouveau_monstre = True


def restart():
    """
    restart() est une fonction qui remet les stats de début du joueur lorsque le celui-ci meurt et que le jeu recommence
    """
    global niveau_vie, numero_combat, nombre_victoires, victoires_consecutives, nombre_defaites, numero_adversaire
    niveau_vie = 20
    numero_combat = 0
    nombre_victoires = 0
    victoires_consecutives = 0
    nombre_defaites = 0
    numero_adversaire = 0


def fight():
    """
    fight() est une fonction qui exécute/définit le code pour l'option 1, c'est-à-dire si le joueur combat le monstre
    """
    global niveau_vie, nombre_victoires, victoires_consecutives, nombre_defaites
    score_de = randint(1, 5) + randint(1, 5)
    print(f"Vous avez lancé un: {score_de}")

    if score_de <= force_adversaire:
        niveau_vie -= force_adversaire
        print(f"Vous avez perdu! Vous avez maintenant {niveau_vie} vies.")
        nombre_defaites += 1
        victoires_consecutives = 0
    elif score_de > force_adversaire:
        niveau_vie += force_adversaire
        print(f"Vous avez gagné! Vous avez maintenant {niveau_vie} vies.")
        nombre_victoires += 1
        victoires_consecutives += 1


jeu_commence = True
while jeu_commence:
    if nouveau_monstre:
        force_adversaire = randint(1, 5) + randint(1, 5)
    else:
        nouveau_monstre = True
    print(f"Vous tombez face à face avec un adversaire de difficulté {force_adversaire}")
    print("voici vos options:")
    print("1- Combattre cet adversaire")
    print("2- Contourner cet adversaire et aller ouvrir une autre porte")
    print("3- Afficher les règles du jeu")
    print("4- Quitter la partie")
    choix_joueur = int(input("Que voulez_vous faire:"))

    if victoires_consecutives == 3:
        numero_combat += 1
        numero_adversaire += 1
        print(f"Adversaire : {numero_adversaire}")
        print(f"Force de l’adversaire : {force_adversaire}")
        force_boss = randint(9, 10)
        victoires_consecutives = 0
        print(f"Vous tombez face à face avec un boss de difficulté {force_boss}")
        fight()

    if choix_joueur == 1:
        numero_combat += 1
        numero_adversaire += 1
        print(f"Adversaire : {numero_adversaire}")
        print(f"Force de l’adversaire : {force_adversaire}")
        print(f"Niveau de vie de l’usager : {niveau_vie}")
        print(f"Combat {numero_combat}  : {nombre_victoires} victoires vs {nombre_defaites} défaites")
        print(f"victoires consécutives  :  {victoires_consecutives}")
        fight()
    elif choix_joueur == 2:
        niveau_vie -= 1
        print("Vous avez choisi d'éviter le combat, donc vous perdez une vie.")
        print(f"Vies:{niveau_vie}")
    elif choix_joueur == 3:
        print("Pour réussir un combat, il faut que la valeur du dé soit supérieure à la force de l’adversaire.")
        print("Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.")
        print("Une défaite a lieu lorsque la valeur du dé est inférieure ou égale à la force de l’adversaire.")
        print("Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.")
        print("La partie se termine lorsque les points de vie de l’usager tombent sous 0.")
        print("L’usager peut combattre ou éviter chaque adversaire")
        print("Cependant, il y a une pénalité de 1 point de vie si vous évitez le combat.")
        nouveau_monstre = False
    elif choix_joueur == 4:
        print("Au revoir!")
        jeu_commence = False
    else:
        print("Cela n'est pas un choix")
        nouveau_monstre = False

    if niveau_vie <= 0:
        """
        Vérifier si joueur mort.
        """
        print(f"GAME OVER! Vous avez vaicu {nombre_victoires} monstres.")
        restart()
