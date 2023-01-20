# Projet 1 - Que de contraintes...

<!--- Changer la date de remise en modifiant le URL--->
#### :alarm_clock: [Date de remise le dimanche 07 Février à 23h59](https://www.timeanddate.com/countdown/generic?iso=20210207T235959&p0=165&msg=INF1007_H21%3A+Projet+1&font=cursive)

## Objectif
Un circuit RL/RC en électrocinétique est un circuit linéaire contenant une résistance et une bobine (inductance)/ une résistance et un condensateur (capacité). 

Il existe deux types de circuits RL/RC série ou parallèle, selon l'interconnexion des deux types de composants. Le comportement des circuits RL ou RC est modélisé par des équations différentielles du premier ordre.

À l'aide d'un générateur de signaux, on peut injecter dans le circuit des oscillations et observer dans certains cas une résonance, caractérisée par une augmentation du courant (lorsque le signal d'entrée choisi correspond à la pulsation propre du circuit, calculable à partir de l'équation différentielle qui le régit). 

Dans un dipôle linéaire, pas forcément élémentaire, mais constitué d'un assemblage d'éléments linéaires passifs R, L, C si l'on prend l'équation qui lie la tension au courant et que l'on y applique une tension ![\bar{U}=U.e^{j(\omega%20t%20-\phi)}](https://latex.codecogs.com/svg.latex?\bar{U}=U.e^{j(\omega%20t%20-\phi)}) , on obtiendra un courant ![\bar{I}=I.e^{j(\omega%20t%20-\phi)}](https://latex.codecogs.com/svg.latex?\bar{I}=I.e^{j(\omega%20t%20-\phi)}) 

On appelle impédance complexe du dipôle la quantité: ![\bar{Z}=\bar{U}/\bar{I}](https://latex.codecogs.com/svg.latex?\bar{Z}=\bar{U}/\bar{I}) 

À quoi sert la notion d'impédance? Si on connaît le module Z et un argument 𝜑 du dipôle, on peut immédiatement passer de la tension au courant ou réciproquement: le module Z indique le rapport entre l'amplitude de la tension et celle du courant. 

Un argument 𝜑 donne quant à lui le déphasage entre la tension et le courant. 

𝜔 représente la pulsation du signal électrique, avec 𝜔 = 2𝜋𝑓 ; 𝑓 étant la fréquence du signal exprimée en Hertz (Hz).

L'objectif du projet est de concevoir et implémenter un programme permettant de calculer l'impédance totale d'un circuit RL/RC.
Pour ce faire, vous devez compléter les deux programmes `impedance_RL.py` et `impedance_RC.py`.

## Important!

Voici quelques fonctions du module math en python qui vous seront utiles!

import math

![\Large \sqrt{x}](https://latex.codecogs.com/svg.latex?\Large&space;\sqrt{x}) correspond à math.sqrt(x)

![\Large e^x](https://latex.codecogs.com/svg.latex?\Large&space;e^x) correspond à math.exp (x)

![\Large \arctan{x}](https://latex.codecogs.com/svg.latex?\Large&space;\arctan{x}) correspond à math.atan(x)


## Partie 1 : impédance RL
À faire : compléter le fichier `impedance_RL.py`

En considérant les données fournies dans le fichier `impedance_RL.py`, vous devez écrire un programme permettant de calculer l'impédance du circuit RL série/parallèle. Vous devrez au préalable calculer l'impédance de l'inductance et par la suite calculer l'impédance équivalente en coordonne polaire.

Voici les équations nécessaires pour la réalisation de l'exercice:

![\Large \omega=2\pif](https://latex.codecogs.com/svg.latex?\Large&space;\omega=2\pi.f) 

![\Large X_L=\omega*L](https://latex.codecogs.com/svg.latex?\Large&space;X_L%20=%20\omega%20*%20L)

![\Large Z_{RL_{serie}}=\sqrt{R^2+X_L^2}](https://latex.codecogs.com/svg.latex?\Large&space;Z_{RL_{serie}}=\sqrt{R^2+X_L^2})

![\Large Z_{RL_{parallel}}=\dfrac{1}{\sqrt{\dfrac{1}{R^2}+\dfrac{1}{X_L^2}}}](https://latex.codecogs.com/svg.latex?\Large&space;Z_{RL_{parallel}}=\dfrac{1}{\sqrt{\dfrac{1}{R^2}+\dfrac{1}{X_L^2}}}) 

![\Large \phi_{RL_{serie}}=\arctan{\left(\dfrac{X_L}{R}\right)](https://latex.codecogs.com/svg.latex?\Large&space;\phi_{RL_{serie}}=\arctan{\left(\dfrac{X_L}{R}\right))


![\Large \phi_{RL_{parallel}}=\arctan{\left(\dfrac{R}{X_L}\right)](https://latex.codecogs.com/svg.latex?\Large&space;\phi_{RL_{parallel}}=\arctan{\left(\dfrac{R}{X_L}\right))

En coordonnées polaires:
![\Large Z_{RL}=Z_{RL}*e^\phi](https://latex.codecogs.com/svg.latex?\Large&space;Z_{RL}=Z_{RL}*e^\phi)

Exemple d'affichage :
```
Module impédance RL série : ... Ohm
Phase impédance RL séries : ... Deg
Impédance  RL série:  Ohm

Module impédance  RL parallèle : ... Ohm
Phase impédance RL séries : ... Deg
Impédance  RL parallèle : ... Ohm
```

## Partie 2 : Optimisation de contraintes
À faire : compléter le fichier `impedance_RC.py`

En considérant les données fournies dans le fichier `impedance_RC.py`, vous devez écrire un programme permettant de calculer l'impédance du circuit RC série/parallèle. Vous devrez au préalable calculer l'impédance de l'inductance et par la suite calculer l'impédance équivalente en coordonne polaire.


![\Large X_C=\dfrac{1}{\omega.C}](https://latex.codecogs.com/svg.latex?\Large&space;X_C=\dfrac{1}{\omega.C}) 

![\Large Z_{RC_{serie}}=\sqrt{X_C^2+R^2}](https://latex.codecogs.com/svg.latex?\Large&space;Z_{RC_{serie}}=\sqrt{X_C^2+R^2})

![\Large Z_{RC_{parallel}}=\dfrac{1}{\sqrt{\dfrac{1}{R^2}+\dfrac{1}{X_C^2}}}](https://latex.codecogs.com/svg.latex?\Large&space;Z_{RC_{parallel}}=\dfrac{1}{\sqrt{\dfrac{1}{R^2}+\dfrac{1}{X_C^2}}}) 

![\Large \phi_{RC_{serie}}=\arctan{\left(-\dfrac{X_C}{R}\right)](https://latex.codecogs.com/svg.latex?\Large&space;\phi_{RC_{serie}}=\arctan{\left(-\dfrac{X_C}{R}\right)})

![\Large \phi_{RC_{parallel}}=\arctan{\left(-\dfrac{R}{X_C}\right)](https://latex.codecogs.com/svg.latex?\Large&space;\phi_{RC_{parallel}}=\arctan{\left(-\dfrac{R}{X_C}\right)})

En coordonnées polaires:
![\Large Z_{RL}=Z_{RL}*e^\phi](https://latex.codecogs.com/svg.latex?\Large&space;Z_{RC}=Z_{RC}*e^\phi)

Exemple d'affichage :
```
Module impédance RC série : ... Ohm
Phase impédance RC séries : ... Deg
Impédance  RC série:  Ohm

Module impédance  RC parallèle : ... Ohm
Phase impédance RC parallèle : ... Deg
Impédance  RC parallèle : ... Ohm
```
