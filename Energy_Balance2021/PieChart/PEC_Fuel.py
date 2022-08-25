import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import patches


 #########       GENERATE FIGURE         ##########

fig = plt.figure(figsize=(12,9))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

 #########      GENERATE DATAFRAME (PIE CHART)  #########

#1st Pie Chart
Energies1 = '','','','LPG(3.28%)','Jet A1(2.27%)',''
Generation1 = [53.37, 27.76, 12.46, 2.90, 2.46, 0.505]
Colors1 = ['Teal', '#269393', '#42a1a1', '#67b3b3', '#bbdddd', '#ffcc00']
explode1 = (0.001, 0.01, 0.01, 0.01, 0.01, 0.1)

#2nd Pie Chart
Energies2 = '','','Solar Thermal(0.04%)','Fuelwood(0.03%)','Kerosene(0.01%)','Avgas(0.005%)'
Generation2 = [2.3, 1.9, 0.4, 0.3, 0.1, 0.05]
Colors2 = ['#ffa600', '#ffb833', '#ffc966', '#ffdb99', '#ffedcc', '#ffffff']
explode2 = (0.001, 0.01, 0.01, 0.01, 0.01, 0.01)

 #########      GENERATE GRAPHIQUE      ##########

ax1.axis([0, 2.4, 0, 2.4])
ax1.pie(x=Generation1, labels=Energies1, colors=Colors1,
        labeldistance=1.1, #or None
        #explode=explode1,
        autopct=None, #or None
        shadow=False, startangle=-0, counterclock=False, frame=False,
       #center=(1.2,1.2),
        wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' },
        textprops = {'fontsize': 13, 'color': 'black'},
        )

ax2.pie(x=Generation2, labels= Energies2, labeldistance=1.05, colors= Colors2,
        #explode=explode2,
        autopct=None, shadow=False, startangle=-0, counterclock=False, frame=False,
        #center=(1.2,1.2),
        wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' },
        textprops = {'fontsize': 12, 'color': 'black'}
        )


 ########       GENERATE TEXT&OBJECT     ##########

plt.text(-3.4,0.6,"Gasoil\n(27.67%)",
         fontsize=20,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )

plt.text(-3.0,-0.4,"Fuel Oil\n(53.37%)",
         fontsize=20,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )

plt.text(-2.5,0.55,"Gasoline\n(12.46%)",
         fontsize=14,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )

plt.text(-0.4,0.5,"Wind\n(0.34%)",
         fontsize=20,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
plt.text(-0.01,-0.4,"Solar PV\n(0.38%)",
         fontsize=20,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None

        )
fig.add_artist(patches.Rectangle((0.57, 0.255), 0.31, 0.48,                    #Position de l'object entre parenthese, le reste sont les dimention x et y
                edgecolor = 'black', facecolor = 'orange',
                fill = False,
                alpha = 0.5,
                #hatch = '/',
                #linestyle = 'dashed',
                linewidth = 1, zorder = 1))

fig.add_artist(patches.Rectangle((0.44, 0.498), 0.132, 0,                    #Position de l'object entre parenthese, le reste sont les dimention x et y
                edgecolor = 'black', facecolor = 'orange',
                fill = False,
                angle = -5.5,
                alpha= 0.6,
                #hatch = '/',
                #linestyle = 'dashed',
                linewidth = 1.2, zorder = 1))

fig.add_artist(patches.Rectangle((0.44, 0.498), 0.132, 0,                    #Position de l'object entre parenthese, le reste sont les dimention x et y
                edgecolor = 'black', facecolor = 'orange',
                fill = False,
                angle = 5.5,
                alpha=0.6,
                #hatch = '/',
                #linestyle = 'dashed',
                linewidth = 1.2, zorder = 1))
#plt.title('Store Inventory')
#plt.ylabel('Product')
#plt.xlabel('Quantity')

 ########       SAVE FIGURE     ##########

plt.savefig('AllFuel2020.png', transparent=True, dpi=300)
plt.show()