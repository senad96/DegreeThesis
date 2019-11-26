import numpy as np 
import modello_fisico as model 
#import modello_pendolo as model
import json
from scipy.constants import G
from params import *
#from params_pendolo import *


def conc(x,y):
    return np.concatenate((x,y));


def evolve():
    
    with open("valori_RK4.txt" , mode='w' ) as f:
    
        yn_rk = model.condizioni_iniziali()
        
        raggio = np.linalg.norm(yn_rk[0:Ndims])  #raggio dalle varibli lagran..
        
        yn_rk = np.append(yn_rk,raggio) #aggiungo il raggio 
        json.dump(yn_rk.tolist(), f)
        f.write('\n')
        
        for i in range(1,x_intervallo):

            t = (i-1)*h_inter # tempo attuale
            
            yn_rk_x = yn_rk[0:Ndims]  #posizione attuale
    
            yn_rk_v = yn_rk[Ndims:2*Ndims]  #velocita attuale ( sarebbe dx/dt ) 
            
            pos = yn_rk_x
            vel = yn_rk_v
    
            t1 = t

            k1v = model.calcola_accelerazioni(conc(pos,vel), t1)*h_inter
    
            k1x = vel*h_inter
    
            t2 = t + h_inter*0.5

            k2v = model.calcola_accelerazioni(conc((pos + k1x*0.5),vel), t2)*h_inter
    
            k2x = (vel+k1v*0.5)*h_inter
    
            t3 = t2

            k3v = model.calcola_accelerazioni(conc((pos+k2x*0.5),vel), t3)*h_inter
    
            k3x = (vel+k2v*0.5)*h_inter
    
            t4 = t + h_inter

            k4v = model.calcola_accelerazioni(conc((pos+k3x),vel), t4)*h_inter
    
            k4x = (vel+k3v)*h_inter
    
            yn_rk_v = yn_rk_v + 1./6.*(k1v+2*k2v+2*k3v+k4v) #vel nuova
    
            yn_rk_x = yn_rk_x + 1./6.*(k1x+2*k2x+2*k3x+k4x) #pos nuova
            
            yn_rk = np.concatenate((yn_rk_x,yn_rk_v))
            
            raggio = np.linalg.norm(yn_rk_x)   # raggio
            
            yn_rk = np.append(yn_rk,raggio)
            
            #print(np.linalg.norm(yn_rk[0:Ndims]))
            
            if np.linalg.norm(yn_rk[0:Ndims]) - raggio_terrestre < 0 :
                
                break
            
            json.dump(yn_rk.tolist(), f)
            f.write('\n')
        
        return
