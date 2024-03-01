import random

def creer_grille(taille):
    return [[" " for _ in range(taille)] for _ in range(taille)]

def afficher_grille(grille):
    for ligne in grille:
        print("|".join(ligne))
        print("-" * (4 * len(ligne) - 1))

def poser_pion(grille, ligne, colonne, symbole):
    if grille[ligne][colonne] == " ":
        grille[ligne][colonne] = symbole
        return True
    else:
        return False

def verifier_victoire(grille, symbole):
    taille = len(grille)
    for i in range(taille):
        if all(grille[i][j] == symbole for j in range(taille)) or all(grille[j][i] == symbole for j in range(taille)):
            return True
    if all(grille[i][i] == symbole for i in range(taille)) or all(grille[i][taille - i - 1] == symbole for i in range(taille)):
        return True
    return False

def coup_aleatoire(grille, symbole):
    taille = len(grille)
    while True:
        ligne = random.randint(0, taille - 1)
        colonne = random.randint(0, taille - 1)
        if grille[ligne][colonne] == " ":
            grille[ligne][colonne] = symbole
            break

def tour_joueur(grille, symbole):
    while True:
        ligne = int(input("Entrez le numéro de ligne (0 à {}): ".format(len(grille) - 1)))
        colonne = int(input("Entrez le numéro de colonne (0 à {}): ".format(len(grille) - 1)))
        if 0 <= ligne < len(grille) and 0 <= colonne < len(grille):
            if poser_pion(grille, ligne, colonne, symbole):
                break
            else:
                print("Cette case est déjà occupée !")
        else:
            print("Position invalide !")

def coup_ordinateur_intelligent(grille, symbole_joueur, symbole_ordi):
    taille = len(grille)
    for i in range(taille):
        for j in range(taille):
            if grille[i][j] == " ":
                grille[i][j] = symbole_ordi
                if verifier_victoire(grille, symbole_joueur):
                    grille[i][j] = symbole_ordi
                    return
                else:
                    grille[i][j] = " "
    coup_aleatoire(grille, symbole_ordi)

def tour_ordi_intelligent(grille, symbole_joueur, symbole_ordi):
    print("Tour de l'ordinateur...")
    coup_ordinateur_intelligent(grille, symbole_joueur, symbole_ordi)

def jeu_morpion(taille):
    grille = creer_grille(taille)
    symboles = ['X', 'O']
    joueur = 0

    while True:
        afficher_grille(grille)
        symbole = symboles[joueur]
        
        if symbole == 'X':
            tour_joueur(grille, symbole)
        else:
            tour_ordi_intelligent(grille, 'X', 'O')

        if verifier_victoire(grille, symbole):
            afficher_grille(grille)
            print("Le joueur {} a gagné !".format(symbole))
            break

        if all(grille[i][j] != " " for i in range(taille) for j in range(taille)):
            afficher_grille(grille)
            print("Match nul !")
            break

        joueur = (joueur + 1) % 2

        print("\n") 

    replay = input("Voulez-vous rejouer ? (o/n) : ")
    if replay.lower() == 'o':
        nouvelle_taille = int(input("Entrez la nouvelle taille de grille : "))
        jeu_morpion(nouvelle_taille)

taille_grille = int(input("Entrez la taille de la grille : "))
jeu_morpion(taille_grille)

