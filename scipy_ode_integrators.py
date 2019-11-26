#import math
from algoritmo_Verlet import *
import json
import numpy as np
from scipy.integrate import *
import modello_fisico as model 
import pandas as pd
from scipy.constants import G
from params import Ndims


class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
            np.int16, np.int32, np.int64, np.uint8,
            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32, 
            np.float64)):
            return float(obj)
        elif isinstance(obj,(np.ndarray,)): #### This is the fix
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


# Non fa altro che applicare il calcolo del modello differenziale
def odeint_derivs(y2,t):
    
    vels = list(y2[Ndims:2*Ndims])
    
    acc = [ model.calcola_accelerazioni(y2, t) ]
    
    return np.append(vels, acc)


def evolve_scipy_odeint():
    
         var_lagrangiane_iniz = model.condizioni_iniziali()
         
         tempi = np.array(range(0,x_intervallo))*h_inter
         y0 = model.condizioni_iniziali()
         
         var_lagrangiane = odeint(odeint_derivs, y0, tempi,hmax=h_inter )
         
         with open("valori_odeint.txt" , mode='w' ) as f:
             
             dumped = json.dumps(var_lagrangiane, cls=NumpyEncoder)
             json.dump(dumped, f)
             
             formatta_file_scipy("valori_odeint.txt")

             return


def formatta_file_scipy(file):    #metodo bruteForce per la codifica.. 
    
    t = open(file)
        
    t1 = t.read()
        
    t2 = t1.replace('"','')
        
    t3 = t2.replace("[","",1)
        
    t4 = t3.rstrip(']')
        
    t5 = t4+']'
        
    s1=t5.replace(']','')
        
    s2=s1.replace('[','')
        
    l = s2.split(',')
    
    t.close()
    
    f2 = open(file,'w')
        
    lista = list(map(float,l))
    
    for i in range(0,len(lista),2*Ndims):
        
        raggio = np.linalg.norm(lista[i:i+Ndims])
        json.dump(lista[i:i+2*Ndims]+[raggio],f2)
        f2.write('\n')
    
    return 
    
        