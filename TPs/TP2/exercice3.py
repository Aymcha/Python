def combinne_dic(dic_1, dic_2):
    # TO-DO: Combinner les deux dictionnaires
    dic_3={}
    for element in dic_2:
        if element in dic_1:
            dic_3[element] = dic_2[element] + dic_1[element]
        else:
            dic_3[element] = dic_2[element]
    for j in dic_1:
        if j not in dic_3:
                dic_3[j] = dic_1[j]
    return dic_3


if __name__ == '__main__':
    dic_1 = {'a':100,'b':200,'c':300}
    dic_2 = {'a':300,'b':200,'d':400}
    dic_3 = combinne_dic(dic_1,dic_2)

