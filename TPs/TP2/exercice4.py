def calculer_pgcd(a, b):

    # TO-DO: Calculer le PGCD
    c = 2
    while c!=0:
      if a < b:
        t = a
        a = b
        b = t

      c = a - b
      a = b
      b = c
    return a


if __name__ == '__main__':
    input_a = int(input("Entrez a: "))
    input_b = int(input("Entrez b: "))
    pgcd = calculer_pgcd(input_a, input_b)
    print(pgcd)
