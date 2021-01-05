# A Comparison of Numerical Algorithms in Applied Physics Simulations


In This Repository you can read and download my *Bachelor's Degree thesis in Computer Science*. I have built an integrator that models 2 physical systems and performs different simulations with different numerical algorithms.



The programming language used is Python and the code is organized in several files, each of which implements an Numerical Algorithm (algoritmo_Eulero.py, algoritmo_RK4.py, algoritmo_Verlet.py ). 

The two system are described through differential equations and the first one model describe the dynamic of a satellite around the earth taking into account the
atmosphere as well. The second model describe the dynimic of a pendulum. Both system are NON-Linear so I've used the numerical algorithms to aproximate the solution
of both system that it would not have been possible to solve through analytic ways.


From 'params_pendolo.py' and 'params_satellite.py' files you can
set system parameters and from file 'evolve.py' you can (by choosing the algorithm) simulate systems.


If you are interested, I would recommend you to read the final report "Relazione_finale.pdf" in PDF ( in Italian, sorry ), where you can find all details about the algorithms and the results.
