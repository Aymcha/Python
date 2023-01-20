def premier(M):
    # TO-DO: determiner les M(i,j) premier
    liste_premier = []
    for i in M:
      for j in i:
          if j==0 or j==1:
             continue
          else:
            for k in range(j- 1, 0, -1):
                if j%k==0:
                    break
          if k==1:
                 liste_premier.append(j)

    return liste_premier


if __name__ == '__main__':

    M_premier = premier(M)
    print(M_premier)
