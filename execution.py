import sys
import tools
import modello_fisico as model
import scipy_ode_integrators
from params import * 



def integrator():
    sys.exit("Unknown method")

def simulazione(method):
    output_dict = {'Eulero': "valori_eulero.txt",
                   'Verlet': "valori_verlet.txt",
                   'RK4': "valori_rk4.txt",
                   'odeint': "valori_odeint.txt"}
    if method == 'Eulero':
        from algoritmo_Eulero import evolve as integrator
    elif method == 'Verlet':
        from algoritmo_Verlet import evolve as integrator
    elif method == 'RK4':
        from algoritmo_RK4 import evolve as integrator
    elif method == 'odeint':
        from scipy_ode_integrators import evolve_scipy_odeint as integrator 
        
    integrator()
    t = model.calcola_energia_meccanica(output_dict[method])
    
    try : 
        if biforcazione == False :
            tools.plotta(output_dict[method], t)
        else:
            return
    except :
        tools.plotta(output_dict[method], t)
    
    
    

   