# Ce programme demande à l'utilisateur son nom et son âge, puis affiche un message de bienvenue
try:

    nom = str (input("Entrez votre nom: "))
    age = int (input("Entrez votre âge (un nombre entier): "))

    # La fonction print contient une erreur de syntaxe
    print("Bonjour, " + nom + " ! Vous avez " + str (age) + " ans.")

    # Une petite erreur de logique ici, l'âge doit être converti en entier pour ajouter 10 ans
    age_plus_10 = age + 10

    print("Dans 10 ans, vous aurez " + str(age_plus_10) + " ans.")
except ValueError:
    print ("value error")
