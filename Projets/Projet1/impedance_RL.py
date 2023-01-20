import math

# Initialisation de variables
f = 60 # en Hz
L = 2*10**-3 # en Henry
R = 50 # en Ohm

# Calcul de omega
w=2*f*math.pi
# Calcul de la réactance inductive
x_l=w*L
# Calcul de l'impédance pour un circuit en parallèle
Z_RLP=1/((1/(R**2))+1/(x_l**2))**0.5
# Calcul de l'impédance pour un circuit en série
z_RLS=(R**2+x_l**2)**0.5
# Calculer phi pour un circuit en série
phi_s=math.atan(x_l/R)
degrees=math.degrees(phi_s)
# Calculer phi pour un circuit en parallèle
Phi_p=math.atan(R/x_l)
degreep=math.degrees(Phi_p)
# Calcul impedance en cordonne polaire
imp_p= Z_RLP*math.exp (Phi_p)
# Calcul impedance en cordonne polaire
imp_s= z_RLS*math.exp (phi_s)

# Affichage de l'impédance pour un circuit en série
print(f"Module impédance RL série : {z_RLS} Ohm")
print(f"Phase impédance RL séries : {degrees} Deg")
print(f"Impédance  RL série: {imp_s} Ohm")

# Affichage de l'impédance pour un circuit en parallèle
print(f"Module impédance  RL parallèle : {Z_RLP} Ohm")
print(f"Phase impédance RL parallèle : {degreep} Deg")
print(f"Impédance  RL parallèle : {imp_p} Ohm")
