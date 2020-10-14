from random import randint

valeurPiece = randint(0,1)
#TODO faire un système avec un bot et un pile ou face contre le bot.
valeurUtilisateur = int(input("Veuillez choisir soit pile soit face avec les valeurs suivantes :\n1 ==> Face\n2 ==> Pile\n"))


if valeurUtilisateur == 1 and valeurUtilisateur == valeurPiece :
    print("La valeur est face, vous avez gagné. Le bot a choisit Pile")
elif valeurUtilisateur == 0 and valeurUtilisateur == valeurPiece :
    print("La valeur est pile, vous avez gagné.")
else : 
    print("Aucune valeur commune, vous avez perdu.")

