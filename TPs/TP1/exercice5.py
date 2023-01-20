

def points_perdu(dindon, lievre, cerf, ours_noir):
    # TODO: Calculer le nombre de points disponible
    nombre_points=100-(5 * cerf + 3 * lievre + 10 * ours_noir + dindon)
    # TODO: Afficher le nombre de points disponible
    print(f'le nombre de points disponibles est {nombre_points}')
    return nombre_points


if __name__ == '__main__':
    dindon = int(input("Entrer le nombre de dindon: "))
    lievre = int(input("Entrer le nombre de lievre: "))
    cerf = int(input("Entrer le nombre de cerf: "))
    ours_noir = int(input("Entrer le nombre d''ours noir: "))
    points_perdu(dindon, lievre, cerf, ours_noir)
