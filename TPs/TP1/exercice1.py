import math


def calculer_portee(angle, vitesse):
    vitesse = vitesse/3.6
    portee = (vitesse**2/9.8)*math.sin(math.radians(2*angle))
    print(f'la valeur de la portée{portee}')
    return portee


if __name__ == '__main__':
    angle = float(input("indiquez l'angle du canon (en deg): "))
    vitesse = float(input("indiquez la vitesse initiale (en km/h) du canon: "))
    calculer_portee(angle, vitesse)