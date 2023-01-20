def multiplication_matrice(A, B):


    # TO-DO: determiner les nombre de Colonne de la matrice A et le nombre de ligne de la matrice B
    Nombre_colonnesA=len(A[0])
    Nombre_lignesB=len(B)
    # TO-DO: Vérifier si la multiplication est possible, si elle n'est pas possible return None
    if Nombre_lignesB!=Nombre_colonnesA:
        return None
    # TO-DO: Effectuer la multiplication matricielle
    else:

       matrice=[]
       for i in range(len(B[0])):
           c=[]
           s=[]
           resultat=[]
           for j in range(len(B)):
               c.append(B[j][i])
           matrice.append(c)

       for f in range(len(A)):
           b = []
           g=0
           while g < len(matrice):
              calcul=0
              for k in range(len(A[0])):
                calcul+=A[f][k]*matrice[g][k]
              b.append(calcul)
              g+=1
           resultat.append(b)
       return resultat









if __name__ == '__main__':
    A = [[2, 3, 6], [5, -1, 12]]
    B = [[1, 0, 4, 7], [2, -3, 6, 2], [5, 8, 9, 6]]
    C = multiplication_matrice(A, B)
    print(C)
