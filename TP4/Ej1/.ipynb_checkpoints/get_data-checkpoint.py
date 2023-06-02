import pandas as pd
import numpy as np

#Paso Inicial
raw_data = pd.read_csv('europe.csv')
data = []
for r in range(len(raw_data)):
  data.append(raw_data.values[r][1:])
data = np.array(data)
medias = []
standard_deviation = []
columns = data.shape[1]

for i in range(columns):
  #Consigo todos los datos de la columna, Xi
  aux = data[:,i]
  #Calculo y guardo su media
  medias.append(np.mean(aux))
  #Calculo y guardo su desviacion estandar
  standard_deviation.append(np.std(aux))
  
#Estandarizo
for i in range(len(data)):
  #Copio la fila
  aux = data[i]
  for j in range(len(aux)):
    #Calculo su valor estandarizado
    standard = (aux[j] - medias[j]) / standard_deviation[j]
    #Lo guardo en la fila
    aux[j] = standard
  #Actualizo la fila en data
  data[i] = aux