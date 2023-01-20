# TP2

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le Dimanche 10 mars 2021 à 23h59](https://www.timeanddate.com/countdown/generic?iso=20210310T2359&p0=165&font=cursive)

## Objectif

Ce TP poursuit votre apprentissage à l'algorithmie avec le langage de programmation Python. Celui-ci est composé de 6 exercices, pour lesquels vous devez compléter le code avec l'indicateur `TODO`.

## Consignes à respecter

Tout d'abord, assurez-vous d'avoir téléchargé les fichiers exercices1-6.py que vous devrez compléter.
Pour ce TP, vous **ne pouvez pas importer d'autres librairies que celle qui sont déjà importées dans les fichiers**.


## Exercice 1:

Dans cet exercice, vous devez écrire un programme qui demande à l’usager de saisir une liste **L** et un nombre entier **Target**. Le programme calcul la somme de deux entiers dans la liste **L** et retourne les indices des deux entiers si leur somme est égale a **Target** et retourne None sinon.

**<ins>Exemple 1:</ins>**
```python
L = [3,2,4]
Target = 6
Indice = [1,2] 
```
**<ins>Exemple 2:</ins>**
```python
L = [3,2,4]
Target = 10
Indice = None 
```

## Exercice 2:

Sois la suite de Fibonacci, définie comme suit:

<p align="center">
     <img src="img/Fino_1.png?raw=true"/>
</p>


Dans cet exercice, vous devez écrire un programme qui demande à l'usager de saisir un nombre entier **P** et qui affiche le plus petit entier **n** tel que:

<p align="center">
     <img src="img/Fino_2.png?raw=true"/>
</p>
 
## Exercice 3:

Dans cet exercice, vous devez écrire un programme qui combine deux dictionnaires en additionnant des valeurs des clés communes.
```python
dic_1 = {'a': 100, 'b': 200, 'c':300}
dic_2 = {'a': 300, 'b': 200, 'd':400}
dic_3 = {'a': 400, 'b': 400, 'd': 400, 'c': 300}
```
## Exercice 4:

Dans cet exercice, vous devez écrire un programme qui calcule le **PGCD** de deux nombres saisi par l’utilisateur à l’aide de la méthode des différences successives.

**<ins>Principe de cette méthode:</ins>** si un nombre est un diviseur de **2** nombres **a** et **b (a > b)**, alors il est aussi un diviseur de leur différence **(a – b)**;

**<ins>Exemple:</ins>** calculons le **PGCD** de **36** et **60** à l'aide de la méthode des différences. Commençons par soustraire **36** de **60**:

**<div align="center"> 60 - 36 = 24</div>**

donc le **PGCD** de **60** et **36** est un diviseur de **24**.

Cherchons alors le **PGCD** de **36** et **24**. Comme la différence obtenue est non nulle, on continue en utilisant le résultat obtenu et le plus petit des **2** termes de la soustraction:

**<div align="center"> 36 - 24 = 12</div>**

La différence est non nulle donc on continue:

**<div align="center"> 24 - 12 = 12</div>**

La différence est non nulle donc on continue:

**<div align="center"> 12 - 12 = 0</div>**

La différence est nulle, on prend le dernier résultat non nul qui est: **12**. On conclut donc que **PGCD(36;60)= 12**.

## Exercice 5:

Dans cet exercice, vous devez écrire un programme qui demande à l'utilisateur de saisir deux matrices **A** et **B** et calcul le produit des deux matrices. Si le nombre de colonnes de la matrice A est diffèrent du nombre de lignes de la matrice B, vous devez retourne None.

**<ins>Exemple 1:</ins>**
```python
A = [[2, 3, 6], [5, -1, 12]]
B = [[1, 0, 4, 7], [2, -3, 6, 2], [5, 8, 9, 6]]
C = multiplication_matrice(A,B) 
  = [[38, 39, 80, 56], [63, 99, 122, 105]]
```
**<ins>Exemple 2:</ins>**
```python
A = [[2, 3, 6], [5, -1, 12]]
B = [[1, 0, 4, 7], [2, -3, 6, 2], [5, 8, 9, 6]]
C = [[38, 39, 80, 56], [63, 99, 122, 105]]
D = multiplication_matrice(C,A) 
  = None
E = multiplication_matrice(B,C) 
  = None
```

## Exercice 6:

Dans cet exercice, vous devez écrire un programme qui demande à l’usager de saisir une matrice **M**, et qui retourne les éléments **M(i,j)** premier.
