def trouver_index_somme(liste_nombre, somme):
    # TO-DO: Trouver l'index
        idx1 = ''
        idx2 = None
        for i in range(len(liste_nombre)):
            for j in range(len(liste_nombre)):
                somme_i_et_j = liste_nombre[i] + liste_nombre[j]
                if i != j and somme_i_et_j == somme:
                    idx1 = i
                    idx2 = j

        if idx1 != '':
          if idx1 > idx2:
            r = idx1
            idx1 = idx2
            idx2 = r
          return idx1, idx2
        else:
          return idx2



if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    idx1, idx2 = trouver_index_somme(nums, target)

