#import execution as ex
import numpy as np
import json
import matplotlib.pyplot as plt
from params_pendolo import *
import file_famp
import evolve 

valori_famp = []
angolo = []

pi = np.pi

for x in np.arange(Famp, famp_max , passo):
    
    evolve.simulazione_('odeint')
    file_famp.famp += passo
    
    valori_famp.append(x)
    
    with open('valori_odeint.txt') as f :
        
        data = []
    
        for line in f:
            data.append(json.loads(line))
        
        angle = data[499][0]
        
        
        while angle>np.pi:
            angle=angle-2*np.pi
            
        while angle<-np.pi:
            angle=angle+2*np.pi
        
        angolo.append(angle)


plt.scatter(valori_famp,angolo,s=0.5,color = 'b')
plt.xlabel('Famp')
plt.ylabel('theta (rad)')
            
        
    
    
