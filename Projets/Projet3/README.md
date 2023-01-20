# Projet 3 - Traitement de text

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimanche 28 mars à 23h59](https://www.timeanddate.com/countdown/generic?iso=20210329T2359&p0=165&font=cursive)

## Objectif
Dans ce projet, vous devez compléter trois aspects de programmation: 
- l'implémentation de fonctions pour résoudre le problème
- la lecture/ecriture de/dans un fichier ".txt".
- implementation de fonction de test unitaire.

### 1. lecture d'un fichier ".txt" (read_file)
Cette fonction doit lire et retourner le contenue du fichier "text.txt" a partir d'un path recu en parametre.

### 2. lecture d'un fichier ".txt" (read_file)
Cette fonction calcule dans un premier temps l'occurrence des mots et les ajoute dans un dictionnaire ainsi que la longueur moyenne des mots du texte puis determine
le mot le plus long/court du texte. La fonction recoit un seul parametre qui est le text lus par la fonction read_file et retourne quatre paremtres: 
- words: dictionnaire des mots du texte
- max_word: le mot le plus long du texte
- min_word: le mot le plus court du texte
- avg_word_text: la longeur moyenne des mots du texte.

### 3. ecriture dans fichier ".txt" (write_file)
Cette fonction dois ecrire les information sur le texte lu par la fonction "read_file" dans le fichier "Result.txt". la fonction a deux paramettre, le premier represente le path du fichier "text.txt" et le second le path du fichiet "Result.txt"

### 4. Tests unitaires 
Afin de vous assurer que votre programme fonctionne bien, vous devez implémenter un test unitaire pour chacune des trois fonctions implémentées, dans le fichier [test_exercice.py](test_exercice.py).


