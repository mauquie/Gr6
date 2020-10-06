class Partie:
    liste_Joueurs = [] #La liste de tout les joueurs de la partie

    def __init__(self):
        pass

    def Jouer(self,nom = "Joueur", main = None, tapis = 500):#Crée un nouveau joueur dans la liste de joueur
        liste_Joueurs =Joueur(nom, main, tapis)
        Partie.liste_Joueurs.append(liste_Joueurs)