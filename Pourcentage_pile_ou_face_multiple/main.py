from random import randint

valeurMaximale = int(input("Veuillez choisir un nombre de fois que vous voudrez tirer la pièce : "))

#Début de la boucle
nombreFace = 0
nombrePile = 0
for i in range (0,valeurMaximale):
    valeurPiece = randint(0,1)
    if valeurPiece == 1 :
        nombreFace = nombreFace + 1
    else:
        nombrePile = nombrePile + 1 
#Fin de la boucle

print(f"vous avez obtenu au total :\n{nombreFace} fois Face\n{nombrePile} fois Pile")

#Calcul de pourcentage
probaPile = (nombrePile * 100) / valeurMaximale
probaFace = (nombreFace * 100) / valeurMaximale

#résultat
print(f"Vous avez obtenu les pourcentages suivants :\n{probaPile}% de Pile\n{probaFace}% de Face")