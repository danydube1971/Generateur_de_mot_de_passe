import random

def generate_password(keyword1, keyword2, keyword3):
    # Combinaison des mots-clés
    keywords = [keyword1, keyword2, keyword3]
    random.shuffle(keywords)
    password = ''.join(keywords)

    # Ajout de caractères aléatoires supplémentaires
    while len(password) < 8:
        password += random.choice(['$', '#', '@', '&', '*', '+', '=', '^'])
    while len(password) > 16:
        password = password[:-1]
    while len(password) < 16:
        password += random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 
                                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
                                   'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '$', '#', '@', '&', 
                                   '*', '+', '=', '^'])

    # Mélange des caractères pour plus de sécurité
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    # Suppression des caractères accentués
    password = password.translate(str.maketrans('', '', 'éèêëàâäïîôöùûüç'))

    # Conversion en minuscules
    password = password.lower()

    return password

# Entrée de l'utilisateur
print("Entrez trois mots-clés pour générer un mot de passe aléatoire.")
keyword1 = input("Mot-clé 1 : ")
keyword2 = input("Mot-clé 2 : ")
keyword3 = input("Mot-clé 3 : ")

# Générer le mot de passe
password = generate_password(keyword1, keyword2, keyword3)

# Affichage du mot de passe
print("Votre mot de passe généré est :", password)

