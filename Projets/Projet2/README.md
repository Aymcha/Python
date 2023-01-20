# Projet 2 - Des films pour le confinement!

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimanche 7 mars à 23h59](https://www.timeanddate.com/countdown/generic?iso=20210309T2359&p0=165&font=cursive)

## Grille de correction
Le projet est sur 20. En lisant les instructions, faites attention à retourner vs afficher. Si vous ne retournez pas ou n'affichez pas ce qui est demandé, il y aura des pénalités. Le choix des structures de données est important dans ce TP. Choisir la mauvaise structure de données mènera à une pénalité.


## Objectif
Pour ce projet, vous devez rechercher un film ou une série dans une base de données multimédia.

Le programme que vous allez implémenter contiendra trois composantes :
1. La première étape est de lire une base de données de films et de séries et de stocker les films et les séries dans une structure de donnée adéquate.
2. Lorsque l'utilisateur fournit un nom de film ou de série, le programme doit retourner tous les noms de films ou de série qui ont ce nom. Par exemple, `har` doit retourner (`Harry Potter`, `Uncharted`, ...)

Pour ce faire, vous devez compléter le fichier `exercice.py`, qui contient 3 fonctions. Vous devez modifier 3 de ces fonctions : `chargement()`, `nettoyer()` et `chercher()` pour lesquelles les définitions vous sont données :

1. ### chargement()

Cette fonction charge en mémoire le contenu de la base de données multimédia.

La base de données est stockée dans un fichier txt nommé `database.txt`. Chaque ligne de ce fichier correspond au type (Film ou Série), au nom et à l'année de sortie. Le code permettant de lire le fichier est déjà implémenté, mais **vous devez compléter la fonction**. Il faudra, en faisant appel à la fonction `nettoyer()`, nettoyer chaque ligne du fichier. Finalement, il faudra choisir le type de structure de données appropriée pour manipuler les données dans le programme. On vous rappelle que l'on veut séparer les films et les séries dans deux structures de données différentes.

On veut retourner les deux structures de données créées.

2. ### nettoyer()

À partir de la ligne passée en paramètre, cette fonction doit retourner une ligne "nettoyée". En d'autres mots, la fonction retourne le type du média(Film/Série), le nom du média en remplaçant "_" par un espace et l'année de production du média.

**Vous devez implémenter cette fonction au complet.** 

3. ### chercher()

Cette fonction doit demander à l'utilisateur quel type de contenu il souhaite rechercher. La question doit lui être posée tant que le choix de l'utilisateur n'est pas valide. Une fois son choix validée, la fonction doit afficher tous les media du type de contenu voulu. Si ce nom est introuvable, la fonction doit afficher `Aucun media trouvé` et retourner `None`.

**Vous devez implémenter cette fonction au complet.**

## Exemple de déroulement du programme

```
>>> Veuillez entrez le type de contenu:Film
>>> Veuillez entrez le nom du contenu à chercher:Harr
harry potter 1 1998
harry potter 2 1999
harry potter 3 1999
harry potter 4 2001
harry potter 5 2003
harry potter 6 2005
harry potter 7 2007

>>> Veuillez entrez le type de contenu:Serie
>>> Veuillez entrez le nom du contenu à chercher:br
breaking bad 2008

>>> Veuillez entrez le type de contenu:Fil
>>> Veuillez entrez le type de contenu:Ser
>>> Veuillez entrez le type de contenu:serie
>>> Veuillez entrez le nom du contenu à chercher:test
Aucun média trouvé
```
