from random import randint


class Cours(object):
    def __init__(self, nom, sigle, nombre_crédits):
        # TODO: à implémenter
        self.nom=nom
        self.crédits=nombre_crédits
        self.sigle=sigle
        self.dictio={}
    def ajout_evaluation(self, nom_eval, ponderation):
        # TODO: à implémenter
        self.nom_eval=nom_eval
        self.ponderation=ponderation
        if self.nom_eval in self.dictio:
           print("L'evaluation existe déjà!")
        else:
            self.dictio[self.nom_eval] = self.ponderation
        return self.dictio
    def __str__(self):
        # TODO: à implémenter
        return f"{self.nom}, {self.sigle}, {self.crédits}"
    def __repr__(self):
        # TODO: à implémenter
        return f'Cours (nom ={self.nom}, sigle ={self.sigle}, credit ={self.crédits})'
class Eleve(Cours):
    def __init__(self, nom_eleve, matricule):
        # TODO: à implémenter
        self.nomeleve=nom_eleve
        self.matricule=matricule
        self.listecours = []
        self.liste = []
    def ajout_cours(self,cours):
        self.cours=cours
        self.listecours.append(str(self.cours).split(','))
        self.liste.append(cours)
    def calculer_note(self):
        # TODO: à implémenter

       print(f"Bulletin de l'eleve {self.nomeleve} ({self.matricule})")
       for i in self.liste:
          print(f"       Pour le cours {i.nom} ({i.sigle}) de {i.crédits} credits ")
          value=0
          for j in i.dictio:
              note=randint(50,100)
              finale=note*i.dictio[j]/100
              value+=finale
              print(f"                 La note obtenu à l'évaluation {j} est {note}%")
          print(f"                 La note obtenu à l'évaluation finale est {round(value,2)}%")
    def __str__(self):
        # TODO: à implémenter
        informationeleve=''
        for i in range(len(self.listecours)):
                informationeleve+=f'{self.listecours[i][0]}, '
        return f"Le nom de l'élève est {self.nomeleve} et son matricule est {self.matricule}. Les cours qu'il prend sont: {informationeleve[:len(informationeleve)-2]}"
    
    def __repr__(self):
        # TODO: à implémenter
       return f'Eleve (nom ={self.nomeleve}, matricule ={self.matricule}, cours ={self.liste})'


if __name__ == "__main__":
    # Création d'élèves
    eleve1 = Eleve("John Doe", 555555)
    eleve2 = Eleve("Jane Doe", 444444)

    # Creation des cours
    cours1 = Cours('Introduction à la programmation', 'INF1007', 4)
    cours2 = Cours('Calcul 1', 'MTH1101', 3)
    cours3 = Cours('Programmation orientée objet avancée', 'INF1015', 4)
    cours4 = Cours('Calcul 2', 'MTH1102', 3)

    # Ajout des cours à l'élève
    eleve1.ajout_cours(cours1)
    eleve1.ajout_cours(cours2)
    eleve2.ajout_cours(cours3)
    eleve2.ajout_cours(cours4)

    # Affichage de l'élève
    print(eleve1)
    print(eleve2)

    # Ajout d'evaluation et calcul de la moyenne de l'élève 1
    cours1.ajout_evaluation('intra', 35)
    cours1.ajout_evaluation('final', 65)
    cours1.ajout_evaluation('intra', 35)
    cours2.ajout_evaluation('intra', 40)
    cours2.ajout_evaluation('final', 60)
    eleve1.calculer_note()

    # Fonction de conversion
    print(cours1.__repr__())
    print(eleve1.__repr__())
