import matplotlib.pyplot as plt
import numpy as np
def xy_txt(carpeta,nombre,col1,col2,xscale,addxmin,addxmax,addymin,addymax,size,xlabel,ylabel):
    filename = carpeta+nombre+'.txt'
    name=carpeta+'fig;'+nombre
    data = open(filename) # open file with names in
    rbfile = data.readline()                # read data file name
    x = np.genfromtxt(filename,skip_header=2,usecols=(col1))
    y = np.genfromtxt(filename,skip_header=2,usecols=(col2))
    xmin=np.min(x)-addxmin
    xmax=np.max(x)+addxmax
    ymin = np.min(y)-addymin
    ymax = np.max(y)+addymax
    plt.plot(x,y,color='black')
    plt.xscale(xscale)
    plt.axis([xmin,xmax,ymin,ymax])
    plt.title(nombre, fontsize=size)
    plt.xlabel(xlabel, fontsize=size)
    plt.ylabel(ylabel, fontsize=size)
    plt.grid(True)
    plt.savefig(name,dpi=300)

# carpeta='/Users/Fede/Desktop/Medicion de micrófonos/'
# nombre='SURE SM57'
# col1=0
# col2=1
# xscale='log'
# xmin=0
# xmax=10000
# ymin=-3
# ymax=3
# size=18
# xlabel='eje x'
# ylabel='eje y'

carpeta='/Users/Fede/Desktop/Medicion de micrófonos/'
nombre='EARTHWORKS 90 GRADOS'
col1=0
col2=1
xscale='log'
addxmin=0
addxmax=100
addymin=-1
addymax=1
size=18
xlabel='Frecuencia [Hz]'
ylabel='Sensibilidad [dB]'

xy_txt(carpeta,nombre,col1,col2,xscale,addxmin,addxmax,addymin,addymax,size,xlabel,ylabel)