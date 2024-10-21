alphabet = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
alphabet_inverse = alphabet [::-1]
print (alphabet_inverse)

ma_string = "Je suis une String"
print (ma_string)

num1 = 40
num2 = 2
print(num1+num2)

num1 = 3
num2 = 14
print(num1*num2)

nom = "coca"
prix_unitaire = 2
inflation = prix_unitaire *10/100
prix_unitaire = prix_unitaire + inflation
quantité_en_stock = 10
quantité_en_stock = quantité_en_stock + 2
requete = int(input("Combien de produit voulez vous ?"))
quantité_en_stock = quantité_en_stock - requete
inventaire = [nom,prix_unitaire,quantité_en_stock]
phrase1 = "Il y a du {0} il coûte {1}€ et il en reste {2}.".format (nom,prix_unitaire,quantité_en_stock)
print (inventaire)
print (requete)
print (phrase1)