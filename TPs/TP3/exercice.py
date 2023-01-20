from random import normalvariate, randint
def lire_classement():
    classement = {}

    # TO-DO: Lire le fichier de classement et insérer les données dans un dictionnaire de dictionnaires.
    with open('database/classement2019.txt', mode='r') as f:
        lines = (line.rstrip() for line in f)
        lines = (line for line in lines if line)
        for row in lines:
               liste=[]
               liste = row.split()
               if liste[0]=='8' or liste[0]=='7':
                 contenu=liste[2:]
                 a=liste[1]
                 classement[a]={}
               else:
                  classement[a][liste[0]]={}
                  données=liste[1:]
                  for i in range(len(données)):
                      classement[a][liste[0]][contenu[i]]=données[i]
    return classement
def lire_match():
    rencontres = []
    # TO-DO: Lire le fichier de matchs et insérer les données dans une liste de listes.
    with open('database/matchs2019.txt', mode='r') as f:
        file_rows = f.readlines()
        for lignes in file_rows:
            liste=lignes.split()
            rencontres.append(liste)
    print(rencontres)
    for parie in rencontres:
       print(parie)
       print(parie[0])
       break
    return rencontres

def trouver_equipe_division(equipe_abv, classement):
    # TO-DO: À l'aide du dictionnaire classement et de l'abbréviation de l'équipe (string),
    classement=lire_classement()
    for i in classement:
        for j in classement[i]:
            for p in classement[i][j]:
                if equipe_abv == classement[i][j][p]:
                   return j,i
def simulation(diffA, diffB):
    # Données à retourner
    pts_equipeA = 0
    pts_equipeB = 0
    but_equipeA = 0
    but_equipeB = 0
    vrp = 1
    # TO-DO: Calculer diff_dom et diff_vis
    diff_dom =(diffB-diffA)/3
    diff_vis =-diff_dom
    # TO-DO: Calculer le nombre de buts de l'equipe à domicile
    alea_d =normalvariate(3 + (diff_dom/100), 1.5)
    # TO-DO: Calculer le nombre de buts de l'equipe visitrice
    alea_v =normalvariate(3+(diff_vis/100), 1.5)
    # TO-DO: Arrondir les nombres de buts
    but_equipeA=round(alea_v)
    but_equipeB=round(alea_d)
    # TO-DO: Décider qui a remporter la victoire
    if but_equipeB>but_equipeA:
        pts_equipeA=0
        pts_equipeB=2
    elif but_equipeB<but_equipeA:
        pts_equipeA=2
        pts_equipeB=0
    else:
       if randint(3, 4)==3:
         vrp=0
       pts_equipeA=2
       pts_equipeB=1
    return pts_equipeA, pts_equipeB, but_equipeA, but_equipeB, vrp
def trier_classement(classement):
    classement_trie = {}
    # TO-DO: Pour chaque division, classer les équipes selon leurs nombres de points. classement est un dictionnaire de
    # dictionnaires.
    for key in classement:
        classement_trie[key] = dict(sorted(classement[key].items(), key=lambda t: int(t[1]['PTS']), reverse=True))
    return classement_trie
def ecrire_classement(classement):
    # TO-DO: Écrire le classement final dans un fichier text
    donnees=simuler_rencontres(ligues_rencontres, ligue_classement)
    with open(classement,'w') as f:
        for key in donnees:
            if key=='Atlantic':
               f.write(str(len(donnees[key])) + ' ' + key + '  ' + 'ABV' + '   ' + 'MJ' + '   ' + 'V' + '    ' + 'D' + '    ' + 'DP' + '  ' + 'PTS' + '  ' + 'VRP' + '  ' + 'BP' + '   ' + 'BC' + '   ' + 'DIFF' + '\n')
            else:
               f.write(str(len(donnees[key]))+'  '+key+'  '+'ABV'+'   '+'MJ'+'   '+'V'+'    '+'D'+'    '+'DP'+'  '+'PTS'+'   '+'VRP'+' '+'BP'+'   '+'BC'+'   '+'DIFF'+'\n')
            for j in donnees[key]:
                a=j
                if key=='Metropolitan':
                    while len(a) < 17:
                        a += ' '
                else:
                    while len(a)<12:
                         a+=' '
                for element in donnees[key][j]:
                    while len(donnees[key][j][element])<3:
                        donnees[key][j][element]=' '+donnees[key][j][element]
                f.write(a+ donnees[key][j]['ABV'] + '  ' + donnees[key][j]['MJ'] + '  ' + donnees[key][j]['V'] + '  ' + donnees[key][j]['D'] + '  ' + donnees[key][j]['DP'] + '  ' +donnees[key][j]['PTS'] + '  ' + donnees[key][j]['VRP'] + '  ' + donnees[key][j]['BP'] + '  ' +donnees[key][j]['BC'] + '  ' + donnees[key][j]['DIFF'] + '\n')
            f.write(' \n')
    f.close()
    # N'oubliez pas d'effacer la ligne pass
def mis_a_jour_classement(equipe, stats, division, classment):
    # TO-DO: Mettre à jour le classement
    for key in classment[division][equipe]:
         if key=='ABV':
             continue
         else:
              classment[division][equipe][key]=str(int(classment[division][equipe][key])+stats[key])
    if int(classment[division][equipe]['DIFF'])>0:
             classment[division][equipe]['DIFF'] = '+' + classment[division][equipe]['DIFF']
    # Trier le classement
    classment = trier_classement(classment)
    return classment
def simuler_rencontres(matchs, classement):
    # Pour chaque match
    matchs=lire_match()
    classement=lire_classement()

    for match in matchs:
        # TO-DO: nom et la division des deux équipes impliquées.
        teamA, division_equipe_A = trouver_equipe_division(match[1], classement)
        teamB, division_equipe_B = trouver_equipe_division(match[0], classement)
        # TO-DO: Simuler une rencontre
        diffA=int(classement[division_equipe_A][teamA]['DIFF'])
        diffB =int(classement[division_equipe_B][teamB]['DIFF'])
        pts_equipeA, pts_equipeB, but_equipeA, but_equipeB, vrp = simulation(diffA,diffB)
        # Créer les dictionnaires stats_equipe_A et stats_equipe_B
        if pts_equipeA>pts_equipeB:
            vA,vB,dA,dB=1,0,0,1
        else:
            vA,vB,dA,dB=0,1,1,0
        if vrp==0 and pts_equipeA>pts_equipeB:
            stats_equipe_A = {'MJ': 1, 'V': vA, 'D': dA, 'DP': 0, 'PTS': pts_equipeA, 'VRP': 1, 'BP': but_equipeA,'BC': but_equipeB, 'DIFF': but_equipeA - but_equipeB}
            stats_equipe_B = {'MJ': 1, 'V': vB, 'D': dB, 'DP': 1, 'PTS': pts_equipeB, 'VRP': 0, 'BP': but_equipeB,'BC': but_equipeA, 'DIFF': but_equipeB - but_equipeA}
        elif vrp==0 and pts_equipeA<pts_equipeB:
            stats_equipe_A = {'MJ': 1, 'V': vA, 'D': dA, 'DP': 1, 'PTS': pts_equipeA, 'VRP': 0, 'BP': but_equipeA,'BC': but_equipeB, 'DIFF': but_equipeA - but_equipeB}
            stats_equipe_B = {'MJ': 1, 'V': vB, 'D': dB, 'DP': 0, 'PTS': pts_equipeB, 'VRP': 1, 'BP': but_equipeB,'BC': but_equipeA, 'DIFF': but_equipeB - but_equipeA}
        else:
           stats_equipe_A = {'MJ':1,'V':vA ,'D':dA,'DP':0,'PTS':pts_equipeA,'VRP':0,'BP':but_equipeA,'BC':but_equipeB,'DIFF':but_equipeA-but_equipeB}
           stats_equipe_B = {'MJ':1,'V':vB ,'D':dB,'DP':0,'PTS':pts_equipeB,'VRP':0,'BP':but_equipeB,'BC':but_equipeA,'DIFF':but_equipeB-but_equipeA}
        classment=mis_a_jour_classement(teamB, stats_equipe_B, division_equipe_B, classement)
        classment=mis_a_jour_classement(teamA, stats_equipe_A, division_equipe_A, classement)
    return classment
if __name__ == '__main__':
    ligue_classement = lire_classement()

    ligues_rencontres = lire_match()

    classement_final = simuler_rencontres(ligues_rencontres, ligue_classement)

    ecrire_classement('classement_final')

