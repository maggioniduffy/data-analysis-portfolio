import numpy as np
import matplotlib.pyplot as plt

plt.style.use('default')

#W = [6.33722925 6.61920409 6.61920409]
#w = [array([-6.3392311 ,  1.61216907,  5.44763428])]    [array([-6.3392311 ,  1.61216907,  5.44763428])]
#w0 = [0.23743639 0.23743639]
#Error = 5.1414191791714545e-06##
def plot(layers,time,method):
    fig, ax = plt.subplots()
    x = np.arange(0,len(layers),1)
    ax.plot(x, layers, linewidth=2.0, label=method)
    ax.legend()
    l = len(x)
    ymax = np.amax(np.array(layers))
    ax.set(xlim=(0, l), xticks=np.arange(0, l),
       ylim=(0, ymax+0.1), yticks=np.arange(0, ymax+0.1, step=0.1))
    
    seconds = str(time).split(':')[-1]
    plt.title('Tiempo: '+str(seconds)+' s')
    plt.ylabel('Error')
    plt.xlabel('Iteraciones')
    plt.show()
    #print("Resultado")
    #print("Metodo: "+ method)
    #print("W = " + str(x[:3]))
    #print("w = "+ str([x[3:6]]) + "\t" + str([x[6:9]]))
    #print("w0 = " + str(x[9:11]))
    #print("Error = " + str(E(x)))
    #print("Tiempo: " + str(time))
