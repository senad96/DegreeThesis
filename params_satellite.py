# Parametri fisici del sistema
Ndims = 3 # Numero delle dimensioni del problema
M1 = 5.972e24  # Kg
m2 = 1200 # Kg
raggio_terrestre = 6371000 #6371000  #metri
altezza = 600000  # in km nell'articolo ma qui in metri 
distanza = raggio_terrestre + altezza
area = 25
#area = 25 # m^2   #si puo scielgiere se mettere None

#parametri del motore/atterraggio
acc_motore = 0   #forza può essere attivata
t_acc = 5000  #secondi
durata = 100   #secondi



# Parametri di integrazione
# h_inter: passo di integrazione
# x_intervallo: intervallo di valutazione della funzione
h_inter = 0.2
x_intervallo = 1000000