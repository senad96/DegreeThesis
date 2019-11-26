import time
from shutil import copyfile

#sciegli il sistema 'satellite' o 'pendolo'
    
sistema = 'pendolo'
    
#Simulazioni
    
metodo1 = 'Eulero'
metodo2 = 'Verlet'
metodo3 = 'RK4'
metodo4 = 'odeint'  


copyfile('params_' + sistema + '.py', 'params.py')

copyfile('modello_' +sistema +'.py' ,'modello_fisico.py')
    
copyfile('tools_' + sistema + '.py', 'tools.py')

from execution import *
    


def simulazione_(metodo):
    
    simulazione(metodo)
    
    return


start_time = time.time()

simulazione_(metodo3)  #sciegli che algoritmo usare in input metodo1/2/3/4

print("--- %s seconds ---" % (time.time() - start_time))

