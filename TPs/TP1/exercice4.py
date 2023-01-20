def convertir_jour(j) :
    return {
        0 : "Dimanche",
        1 : "Lundi",
        2 : "Mardi",
        3 : "Mercredi",
        4 : "Jeudi",
        5 : "Vendredi",
        6 : "Samedi",
    }[j]

def trouver_jour_semaine(annee, mois, jour):
    # TODO: Calculer p
    p = (14 - mois) // 12
    # TODO: Calculer q
    q = annee-p
    
    # TODO: Calculer r
    r = q+(q//4)-(q//100)+(q//400)

    # TODO: Calculer s
    s = mois+12*p-2

    # TODO: Calculer t 
    t = (jour+r+((31*s)//12))%7

    # Convertir le résultat de la formule de Zeller
    jour_semaine = convertir_jour(t)

    # TODO: Afficher le jour de la semaine
    print(f'le jours de la semaine est {jour_semaine} ')
    return jour_semaine

if __name__ == '__main__':
    annee = int(input("Entrer l'annee: "))
    mois = int(input("Entrer le mois: "))
    jour = int(input("Entrer le jour: "))
    trouver_jour_semaine(annee, mois, jour)


