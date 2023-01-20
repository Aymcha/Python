def chargement():
    """
    Cette fonction charge en mémoire le contenu de la base de données des adresses enregistrées.
    """
    # TODO: initialiser la structure de données vide

    with open('data/database.txt', mode='r') as f:
        file_rows = f.readlines()
        film_donnees = {}
        serie_donnees = {}
        for row in file_rows:
            type, nom, annee = nettoyer(row)

            # TODO: Tester le type du média et l'ajouter a la bonne structure de données

            if type=="Film":
                film_donnees[nom.lower()]=annee
            else:
                serie_donnees[nom.lower()]=annee

    return  film_donnees, serie_donnees


def nettoyer(ligne):

	#TODO: séparer la ligne reçue en paramètre en trois variables
    liste=ligne.split()
	# type : pour le type du média
    type=liste[0]
	# nom: Pour le nom du média
    nom=liste[1]
	# annee: pour l'année de production du média
    annee=liste[2]
	# TODO: remplacer le caractère _ dans le nom du média par un espace
    for i in range(len(liste[1])):
        if nom[i]=="_":
            nom=nom[:i]+' '+nom[i+1:]
    return type, nom.lower(), annee
def chercher(film_donnees, serie_donnees):

	# TODO: demander à l'utilisateur de saisir un type de média à rechercher
    type_de_media=input("Saisissez le type de média à rechercher \n")
	# l'utilisateur continue de faire la saisie tant que type ne correspond pas à (film ou série)
    while type_de_media.capitalize()!='Film' and type_de_media.capitalize()!='Serie' and type_de_media.capitalize()!='Série':
          type_de_media=input("Saisissez le type de média à rechercher \n")


	# TODO: demander à l'utilisateur de saisir le nom du média rechercher
    triage = input("Saisissez le nom de média à rechercher \n")

	# TODO: dépendamment du type du média rechercher, on doit chercher le nom du média rechercher dans la bonne
	# structure de données
    selection = {}
    existance = True
    if type_de_media.capitalize()=='Film':
     # TODO: afficher l'ensemble des médias qui contient le nom recherché
        for element in film_donnees:
            if triage.lower() in element:
                selection[element.lower()]=film_donnees[element]
                existance=False
    else:
        for key in serie_donnees:
            if triage.lower() in key:
                selection[key.lower()]=serie_donnees[key]
                existance = False
    # TODO: la fonction retourne True si on trouve au moins un seul média, false sinon
    if  existance:
        print('Aucun média trouvé')
        return None
    else:
        return selection





if __name__ == '__main__':
    film_donnees, serie_donnees = chargement()
    chercher(film_donnees, serie_donnees)