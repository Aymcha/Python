import math

# Initialisation de variables
f = 60 # en Hz
C = 10*10**-6 # en farad
R = 50 # en Ohm

# Calcul de omega

w=2*f*math.pi
# Calcul de la réactance inductive
x_c=1/(w*C)
# Calcul de l'impédance pour un circuit en parallèle
Z_RCP=1/((1/(R**2))+1/(x_c**2))**0.5
# Calcul de l'impédance pour un circuit en série
z_RCS=(R**2+x_c**2)**0.5
# Calculer phi pour un circuit en série
phi_s=math.atan(-x_c/R)
degrees=math.degrees(phi_s)
# Calculer phi pour un circuit en parallèle
Phi_p=math.atan(-R/x_c)
degreep=math.degrees(Phi_p)
# Calcul impedance en cordonne polaire
imp_p= Z_RCP*math.exp (Phi_p)
# Calcul impedance en cordonne polaire
imp_s= z_RCS*math.exp (phi_s)
## Afficher impédence série
print(f"Module impédance RC série : {z_RCS} Ohm")
print(f"Phase impédance RC séries : {degrees} Deg")
print(f"Impédance  RC série: {imp_s} Ohm")

## Afficher impédence parrallèle
print(f"Module impédance  RC parallèle : {Z_RCP} Ohm")
print(f"Phase impédance RC parallèle : {degreep} Deg")
print(f"Impédance  RC parallèle : {imp_p} Ohm")
