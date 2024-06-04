# Ce programme demande à l'utilisateur son nom et son âge, puis affiche un message de bienvenue

nom = input("Entrez votre nom: ")
age = input("Entrez votre âge: ")

# La fonction print contient une erreur de syntaxe
print("Bonjour, " + nom +" ! Vous avez " + age + " ans.")

# Une petite erreur de logique ici, l'âge doit être converti en entier pour ajouter 10 ans
age_plus_10 = int(age )+ 10

print("Dans 10 ans, vous aurez " +str (age_plus_10) + " ans.")
