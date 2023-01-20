

def calculer_unites_dizaines_centaine(nombre):
    # TODO: Déterminer le nombre d'unités et mettre la valeur dans "unites
    entiers= nombre % 10
    # TODO: Déterminer le nombre de dizaines et mettre la valeur dans "dizaines"
    a= ((nombre-entiers)/10)
    dizaines=a%10
    # TODO: Déterminer le nombre de centaines et mettre la valeur dans "centaines"
    b= ((nombre-entiers-dizaines*10)/100)
    centaines=b%10
    # TODO: Afficher les valeurs de "unites", "dizaines" et "centaines"
    print(f'la valeur des unités est {entiers}')
    print(f'la valeur des dizaines est {dizaines}')
    print(f'la valeur des centaines est {centaines}')

    return entiers, dizaines, centaines



if __name__ == '__main__':
    nombre = int(input('veuillez indiquer un nombre strictement postif: '))
    calculer_unites_dizaines_centaine(nombre)