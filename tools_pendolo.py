import numpy as np
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.constants import G
import modello_fisico as md
from params import * 
import execution



def plotta(file,energia):
    
    f = open(file)
    data = []
    
    for line in f:
        data.append(json.loads(line))
    
    data = np.array(data)

    #estrai colonne
    theta = data[:,0]
    omega = data[:,1]
    
    theta2 = []
    #x_int = np.linspace(1,len(energia),len(energia))
    #theta = theta%(2*np.pi)   #modulo per ottenere angoli fra 0 e 360
    
    for angle in theta :
        while angle>np.pi:
            angle=angle-2*np.pi
            
        while angle<-np.pi:
            angle=angle+2*np.pi
        
        theta2.append(angle)
    
    plt.figure(1)
    plt.plot(theta2, omega)
    plt.grid(True)
    plt.title('phase_space')
    
    plt.xlabel('rad')
    plt.ylabel('rad/s')
    
    return



    
    

    
    
    
    
    








