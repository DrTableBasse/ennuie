from random import randint
#choix =[1::pierre;]
#TODO dictionnaire
pierre = 1
papier = 2
cisceaux = 3

choix = int(input("Veuillez choisir une valeur correspondante à votre choix : \npierre = 1\npapier = 2\ncisceaux = 3\n=>"))
choixBot = randint(1,3)
if choix == 1 and choixBot == 2 :
    print("Vous avez perdu, Le bot a choisi Papier")
elif choix == 1 and choixBot == 3 :
    print("Bravo tu as gagné, Le bot a choisi Cisceaux")
elif choix == 2 and choixBot == 1:
    print("Bravo tu as gagné, Le bot a choisi Pierre")
elif choix == 2 and choixBot == 3:
    print("Tu as perdu, Le bot a choisi Cisceaux")
elif choix == 3 and choixBot == 1:
    print("Tu as perdu, le bot a choisi Pierre")
elif choix == 3 and choixBot == 2:
    print("Bravo tu as gagné, le bot a choisi Papier")
elif choix == choixBot:
    print("Egalité")
    


