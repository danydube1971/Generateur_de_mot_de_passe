# Générateur de mot de_passe

Le script génère un mot de passe aléatoire à partir de trois mots-clés ciblés entrés par l'utilisateur. 

Voici les étapes du script :

1. L'utilisateur entre trois mots-clés.
2. Les mots-clés sont combinés de manière aléatoire pour créer une chaîne de caractères.
3. Des caractères aléatoires supplémentaires sont ajoutés à la chaîne de caractères pour créer un mot de passe complexe.
4. Si la longueur du mot de passe dépasse 16 caractères, le dernier caractère est supprimé.
5. Si la longueur du mot de passe est inférieure à 8 caractères, des caractères aléatoires sont ajoutés jusqu'à ce que la longueur minimale soit atteinte.
6. Les caractères du mot de passe sont mélangés pour plus de sécurité.
7. Les caractères accentués sont supprimés de la chaîne de caractères finale.
8. Le mot de passe final est converti en minuscules.
9. Le mot de passe final est affiché à l'utilisateur.

Le résultat est un mot de passe aléatoire complexe qui contient les trois mots-clés entrés par l'utilisateur, 
ainsi que des caractères aléatoires supplémentaires. La longueur du mot de passe final est comprise entre 8 et 16 caractères, 
et il ne contient pas de caractères accentués.

# Comment utiliser ce script
Dans un terminal Linux, exécuter le script avec la commande suivante: 

**python3 "Générateur de mot de passe.py"**



Testé dans Linux Mint 21
