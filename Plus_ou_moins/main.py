import random

max_value = int(input("Veuillez choisir un chiffre de départ : "))
extreme = random.randint(0, max_value)
print(extreme)
print("La valeur est comprise entre 0 et", max_value)

nbUser = int(input("veuillez choisir une valeur entre cet intervalle : "))


while nbUser != extreme :
    

    if nbUser < extreme :
        print ("c'est plus !")
        nbUser = int(input("Réessaye donc en écrivant une nouvelle valeure : "))

    elif nbUser > extreme:
        print("c'est moins !")
        nbUser = int(input("Réessaye donc en écrivant une nouvelle valeure : "))

print("tié un bon toi bravo !")
