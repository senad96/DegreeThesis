from algoritmo_Eulero import passo_eulero_singolo
import modello_fisico as model
import numpy as np
import json
import tools
from params import * 



def passo_verlet(var_lagrangiane, t):

    # Posizione attuale 
    x = var_lagrangiane[0:Ndims]

    # Velocita' attuale 
    v = var_lagrangiane[Ndims:2*Ndims]
    

    # Accelerazione attuale
    a = model.calcola_accelerazioni(var_lagrangiane, t)
    
    # Stima delle nuove variabili lagrangiane con Eulero
    var_lagrangiane_seminew = passo_eulero_singolo( \
        var_lagrangiane, np.append(v,a))
  
    # Accelerazione nuova
    a_new = model.calcola_accelerazioni(var_lagrangiane_seminew, t+h_inter)
    
    # Posizione nuova
    x_new = x + v*h_inter + 0.5*a*h_inter**2

    # Velcotia' nuova
    v_new = v + 0.5*(a_new + a)*h_inter
    
    return np.concatenate((x_new, v_new))
    


def evolve():
    
    with open("valori_verlet.txt" , mode='w' ) as f:
         
         var_lagrangiane = model.condizioni_iniziali()
            
         pos =  var_lagrangiane[:Ndims]
         raggio = np.linalg.norm(pos)
         
         
         var_lagrangiane = np.append(var_lagrangiane,raggio)
         
         json.dump(var_lagrangiane.tolist(), f)
         f.write('\n')
         
         for i in range(1,x_intervallo):
             # Passo in avanti con Verlet 
             var_lagrangiane = passo_verlet(var_lagrangiane[:2*Ndims], (i-1)*h_inter) 
             # Scrittura su file 
             raggio = np.linalg.norm(var_lagrangiane[:Ndims])  #calcolo il raggio dalla pos
             
             var_lagrangiane = np.append(var_lagrangiane,raggio)
             
             if np.linalg.norm(var_lagrangiane[:Ndims]) - raggio_terrestre < 0 : 
                 break
             
             json.dump(var_lagrangiane.tolist(), f)
             f.write('\n')
         return 
