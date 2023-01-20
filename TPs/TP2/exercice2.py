def fibonacci(n):
    # TO-DO: Calculer le neme element de la suite de Fibonacci
    F1 = 1
    F0 = 0
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        for i in range(n-1):
            F2 = F1 + F0
            F0 = F1
            F1 = F2
            i+=1
        return F2
if __name__ == '__main__':
    input_n = int(input("Entrez n: "))
    valeur = fibonacci(input_n)
    print(valeur)
