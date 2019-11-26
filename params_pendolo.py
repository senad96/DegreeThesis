# Parametri fisici del sistema
Ndims = 1 # Numero delle dimensioni del problema
m = 2 # Kg
l = 1.5 # m 
I = 6 # kg*m^2
beta = 1 # Kg/2 
Famp = 10 # N
omega = 2 # rad/s
g = 9.81 
raggio_terrestre = -1 # raggio fittizio per eludere l'algoritmo nel break

#parametti inziali theta0 e omega0
theta0 = 0
omega0 = 0


# Parametri di integrazione
# h_inter: passo di integrazione
# x_intervallo: intervallo di valutazione della funzione
h_inter = 0.01
x_intervallo = 50000

#parametri per la biforcazione
biforcazione = False
famp_max = 10
passo = 0.001

