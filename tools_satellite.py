import numpy as np
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.constants import G
import modello_fisico as md
from params import * 



def plotta(file,energia):
    
    f = open(file)
    data = []
    
    for line in f:
        data.append(json.loads(line))
    
    data = np.array(data)

    #estrai colonne
    x = data[:,0]
    y = data[:,1]
    
    x_int = np.linspace(1,len(energia),len(energia))
    
    if area != None :
        
        plt.figure(1)
        plt.subplot(221)
        plt.plot(x, y)
        plt.grid(True)
        plt.title('Orbita')
        circle = plt.Circle((0,0),md.raggio_terrestre,color ='g',fill=False)
        fig = plt.gcf()
        ax = fig.gca()
        ax.add_artist(circle)
        plt.xlabel('metri')
        
        plt.subplot(222)
        plt.plot(x_int*md.h_inter,energia)
        plt.grid(True)
        plt.title('Energia meccanica')
        plt.xlabel('secondi')
        plt.ylabel('joule')
        
        
        plt.subplot(212)
        altezza = data[:,6] - md.raggio_terrestre
        plt.plot(x_int*md.h_inter,altezza)
        plt.grid(True)
        plt.title('Altezza')
        plt.xlabel('secondi')
        plt.ylabel('metri')
        
    else:
        
        plt.figure(1)
        plt.subplot(221)
        plt.plot(x, y)
        plt.grid(True)
        plt.title('Orbita')
        plt.xlabel('metri')
        
        plt.subplot(222)
        plt.plot(x_int*md.h_inter,energia)
        plt.grid(True)
        plt.title('Energia meccanica')
        plt.xlabel('secondi')
        plt.ylabel('joule')
        
        plt.subplot(223)
        y_2 = (data[:,6] - distanza )/distanza
        plt.plot(x_int*md.h_inter,y_2)
        plt.grid(True)
        plt.title('Errore raggio')
        plt.xlabel('secondi')
        plt.ylabel('Errore relativo')
        
    
        plt.subplot(224)
        energia_cinetica = 0.5*m2*(np.sqrt(G*M1/distanza))**2
        energia_ideale = energia_cinetica - G*M1*m2/distanza
        
        errore_en = (energia - energia_ideale)/energia_ideale
        
        plt.grid(True)
        plt.title('Errore Energia meccanica')
        plt.plot(x_int*md.h_inter,errore_en)
        plt.xlabel('secondi')
        plt.ylabel('Errore Relativo')
    
    return 

    







