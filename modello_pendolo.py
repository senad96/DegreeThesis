import numpy as np
from scipy.constants import G # costante gravitazionale
import json
from params import * 
import file_famp as fp

# Modello fisico
def calcola_accelerazioni(var_lagrangiane, t):

    vel = var_lagrangiane[1]  #vel ang
    pos = var_lagrangiane[0]  #angolo
    
    famp = fp.famp #assegnamento utile per il grafico di biforcazione
    
    a = -(beta/I)*vel - (m*g*l/I)*np.sin(pos)+(famp)*np.cos(omega*t)  
    

    return a 
    

################

def condizioni_iniziali():
    
    pos_iniziale = theta0 #rad
    vel_iniziale = omega0#rad/s
    
    var_lagrangiane = [pos_iniziale,vel_iniziale] #pos e vel iniziale angolare 

    return var_lagrangiane



def calcola_energia_cinetica(var_lagrangiane):

    return 0.5*m*(np.linalg.norm(var_lagrangiane[Ndims:2*Ndims]))**2


# FIXME: questa sara' model-dependent...
def calcola_energia_potenziale(var_lagrangiane):
    return 0

# ... ma questa no.
def calcola_energia_meccanica(file):
    
    energia = []
    t = open(file)
    
    for line in t: 
        l = json.loads(line)
        var_lagrangiane = np.array(l)
        #calcolo energia meccanica da ciascun dato poiche ho le vx,vy
        val = calcola_energia_cinetica(var_lagrangiane) + calcola_energia_potenziale(var_lagrangiane)
        
        energia.append(val)
        
    return np.array(energia)