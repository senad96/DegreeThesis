# A Comparison of Numerical Algorithms in Applied Physics Simulations


In This Repository you can read and download my **Bachelor's Degree thesis in Computer Science**. I have built an integrator that models 2 physical systems and performs different simulations with different numerical algorithms.


# Abstract

Differential equations are very powerful tools that play a fundamental role in describing a multitude of phenomena of different nature and are therefore the most used equations in Physics, Mathematics and Engineering. In applications it is extremely hard to solve a differential equation. Indeed, except in rare cases, the explicit solution cannot be determined analytically.
In this project I will describe some basic techniques and algorithms that are used to approximate the solution of systems of ordinary differential equations. In particular, the different performances of numerical algorithms will be compared in two cases of non-linear dynamics :

1. The motion of a satellite in an atmosphere
1. The temporal evolution of a compound pendulum subjected to a external force.

The importance of the algorithms themselves in the study and simulation of dynamic systems will be discussed.
For a greater understanding of simulation methods and for greater comparison among the various algorithms, we have implemented some 
methods from scratch, creating a integrator for the two physical systems considered. The language used is Python.





# Code

The program has been split into various files for more readability and organization. In two different files, *params_satellite.py* and
*params_pendio.py*, the parameters of the systems and algorithms are located. For example, by choosing the parameters in *param_pandolo.py* you can decide whether or not to make the friction appear in the system and whether to activate the driving force ( pendulum ). In the *evolve.py* file you can decide which dynamic system to evolve : more precisely, the value of the *system* variable can be set in "satellite" or "pendolo".
Furthermore, by deciding which input to give to the function *simulazione_(method1, method2, method3, method4)*, the algorithm to be used for the simulation is selected. "metodo1" corresponds to Euler, "metodo2" Verlet algorithm, "metodo3" RK4 algorithm and lastly "metodo4" indicates the use of the odeint function of the Scipy library. 

At this point, running the *evolve.py* file with the right parameters will start the simulation of the desired system, according to the selected algorithm.


# More Details

If you are interested, I would recommend you to read the final report "Relazione_finale.pdf" in PDF ( in Italian, sorry ), where you can find all details about the algorithms and the results.
