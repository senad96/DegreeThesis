import numpy as np
import json
from scipy.constants import G
import modello_fisico as model
from params import * 


def passo_eulero_singolo(x, dxdt):
    
    x_new = x + h_inter*dxdt
    
    return x_new



def evolve():

    with open("valori_eulero.txt" , mode='w' ) as f:

        var_lagrangiane = model.condizioni_iniziali()
        
        raggio = np.linalg.norm(var_lagrangiane[:Ndims])
        
        var_lagrangiane = np.append(var_lagrangiane,raggio)  #aggiungo raggio
        
        json.dump(var_lagrangiane.tolist(), f)
        f.write('\n')
        
        for i in range(1,x_intervallo):
            # Poszione attuale
            pos = var_lagrangiane[0:Ndims]
            # Velocita' attuale
            vel = var_lagrangiane[Ndims:2*Ndims]
            
            # Accelerazione attuale
            acc =  model.calcola_accelerazioni(var_lagrangiane[:2*Ndims], h_inter*(i-1))
            
            
            # Aggiorna posizione e velocita'
            var_lagrangiane = \
            passo_eulero_singolo( np.append(pos, vel), \
                                 np.append(vel, acc)) 
            
            pos = var_lagrangiane[:Ndims]
            
            raggio = np.linalg.norm(pos)
            
            var_lagrangiane = np.append(var_lagrangiane, raggio)
            
            if np.linalg.norm(pos[0:Ndims]) - raggio_terrestre < 0 :
                break
            
            json.dump(var_lagrangiane.tolist(), f)
            f.write('\n')
            
        return
