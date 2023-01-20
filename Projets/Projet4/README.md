# Projet 4 - Registrariat de Poly a besoin d'aide

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimanche 18 avril à 23h59](https://www.timeanddate.com/countdown/generic?iso=20201206T2359&p0=165&msg=Remise&font=cursive&csz=1#)

## Objectif
Poly veut changer le système de gestion des notes. Pour cela, ils font appel à vous!

Dans ce projet, vous devez implémenter une classe `Cours` avec les propriétés suivantes :
- Un cours est représenté par un nom, un sigle, un nombre de crédits et un dictionnaire d'évaluation. Ce dictionnaire a comme clé le nom de l'évaluation et comme valeur sa pondération.
- La classe `Cours` définit un constructeur qui prend en entrée son nom, son sigle et les crédits du cours. Le dictionnaire d'évaluation est vide au départ.
- La classe `Cours` implémente une fonction ```ajout_evaluation(self, nom_eval, ponderation)``` qui permet d'ajouter une évaluation au dictionnaire. L'évaluation doit être unique au cours. Sinon, un message d'erreur doit être affiché.
- une fonction de conversion `__str__` permettant d'avoir le nom du cours, son sigle et son nombre de crédits sous la forme suivante: `NOM DU COURS (SIGLE) de X credits`. Par exemple `Introduction à la programmation (INF1007) de 4 credits`.
- une fonction de conversion `__repr__` retournant la classe et la valeur des attributs du cours sauf l'attribut evaluations. Par exemple: `Cours(nom=Introduction à la programmation, sigle=INF1007, credit=INF1007)`

La classe `Eleve` est une classe très simple qui doit implémenter les caractéristiques suivantes :
- un constructeur qui prend en entrée son nom, sous la forme d'une chaîne de caractère, et son sigle. Elle doit aussi initialiser une liste de cours vide au départ,
- une fonction `ajout_cours(self, cours)` qui permet d'ajouter un cours à la liste de cours,
- une fonction `calculer_note(self)` qui donne une note aléatoire entre 50 et 100 pour chaque évaluation de l'élève et calcule la note de chaque cours.
- une fonction de conversion `__str__` permettant d'afficher le nom de l'élève, son matricule et les cours qu'ils prends. Par exemple, `Le nom de l'eleve est John Doe et son matricule est 555555. Les cours qu'il prends sont: Introduction à la programmation, Calcul 1`
- une fonction de conversion `__repr__` retournant la classe et la valeur des attributs de l'élève. Par exemple `Eleve(nom=John Doe, matricule=555555, cours=[Cours(nom=Introduction à la programmation, sigle=INF1007, credit=INF1007, Cours(nom=Calcul 1, sigle=MTH1101, credit=MTH1101])`

Dans ce projet, vous devez compléter le fichier `exercice.py`. Le bloc d'instruction dans la fonction `main` vous montre un cas concret d'utilisation du programme, qui evrait vous fournir un affichage tel que présenté ci-dessous :

```
Le nom de l'eleve est John Doe et son matricule est 555555. Les cours qu'il prends sont: Introduction à la programmation, Calcul 1 
Le nom de l'eleve est Jane Doe et son matricule est 444444. Les cours qu'il prends sont: Programmation orientée objet avancée, Calcul 2 
L'evaluation existe déjà!
Bulletin de l'eleve John Doe (555555)
	Pour le cours Introduction à la programmation (INF1007) de 4 credits
		La note obtenu à l'évaluation intra est 54%
		La note obtenu à l'évaluation final est 64%
		La moyenne du cours est 60.5%
	Pour le cours Calcul 1 (MTH1101) de 3 credits
		La note obtenu à l'évaluation intra est 92%
		La note obtenu à l'évaluation final est 71%
		La moyenne du cours est 79.4%
Cours(nom=Introduction à la programmation, sigle=INF1007, credit=INF1007)
Eleve(nom=John Doe, matricule=555555, cours=[Cours(nom=Introduction à la programmation, sigle=INF1007, credit=INF1007), Cours(nom=Calcul 1, sigle=MTH1101, credit=MTH1101)])
```
