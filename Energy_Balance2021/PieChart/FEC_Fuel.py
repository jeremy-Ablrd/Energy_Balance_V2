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
Energies1 = '','','','LPG(5.41%)','Fuel Oil(4.5%)','Jet A1(1.7%)', ''
Generation1 = [40.4, 23.9, 23.9, 5.41, 4.5, 1.7, 0.5]
Colors1 = ['#00b386', '#269393', '#42a1a1', '#67b3b3', '#bbdddd','#ffffff', '#ffcc00']
explode1 = (0.001, 0.01, 0.01, 0.01, 0.01, 0.1)

#2nd Pie Chart
Energies2 ='','','',''
Generation2 = [1, 0.6, 0.59, 0.2]
Colors2 = ['#ffa600', '#ffb833', '#ffc966', '#ffdb99']
explode2 = (0.001, 0.01, 0.01, 0.01, 0.01, 0.5)

 #########      GENERATE GRAPHIQUE      ##########

ax1.axis([0, 2.4, 0, 2.4])
ax1.pie(x=Generation1, labels=Energies1, colors=Colors1,
        labeldistance=1.05, #or None
        #explode=explode1,
        autopct=None, #or None
        shadow=False, startangle=-0, counterclock=False, frame=False,
       #center=(1.2,1.2),
        wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' },
        textprops = {'fontsize': 14, 'color': 'black'},
        )

ax2.pie(x=Generation2, labels= Energies2, labeldistance=0.3, colors= Colors2,
        #explode=explode2,
        autopct=None, shadow=False, startangle=-0, counterclock=False, frame=False,
        #center=(1.2,1.2),
        wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' },
        textprops = {'fontsize': 12, 'color': 'black'}
        )


 ########       GENERATE TEXT&OBJECT     ##########

plt.text(-3.55,0.2,"Gasoline\n(23.9%)",
         fontsize=18,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
plt.text(-2.8,-0.4,"Electricity\n(40.4%)",
         fontsize=20,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
plt.text(-3,0.69,"Gasoil\n(23.9%)",
         fontsize=18,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
         )
plt.text(0.70,0.25,"Kerosene\n(0.02%)",
         fontsize=15,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
plt.text(-0.01,-0.4,"Solar Heat\n(0.1%)",
         fontsize=18,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
         )
plt.text(-0.55,0.3,"Biomass\n(0.06%)",
         fontsize=18,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
         )

plt.text(0.2,0.7,"Avgas\n(0.059%)",
         fontsize=18,
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

plt.savefig('AllFEC2020.png', transparent=True, dpi=300)
plt.show()