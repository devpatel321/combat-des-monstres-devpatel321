"""
Créé par Dev Patel du groupe 402
Créé le 29 septembre 2022
Créer
"""

from random import randint

jeu_commence = True
while jeu_commence:

    niveau_vie = 20
    force_adversaire_1 = randint(1, 5)
    force_adversaire_2 = randint(1, 5)

    print(f"Vous tombez face à face avec un adversaire de difficulté {force_adversaire_1 + force_adversaire_2}, voici vos options: \n1- Combattre cet adversaire \n2- Contourner cet adversaire et aller ouvrir une autre porte \n3- Afficher les règles du jeu \n4- Quitter la partie")
    question_1 = input("Que voulez_vous faire:")







