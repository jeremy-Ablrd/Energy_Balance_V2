import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import seaborn as sns

#generate figure
plt.figure(figsize=(12,9))

#generate dataframe for pie plot
Energies = 'Fuel Oil', 'Wind Farm', 'Solar PV'
Electricity_Generation = [86.7+10.4, 1.4, 1.5]
Colors = ['Teal', '#a3b825','#fad335']
explode = (0.25, 0, 0)
#generate graphique

#plt.plot(x,y)
#plt.axis([0, 2.4, 0, 2.4])
plt.pie(x= Electricity_Generation, labels= Energies, labeldistance=None, colors= Colors,
        autopct=None, shadow=False, startangle=-0, counterclock=False, frame=False, center=(1.2,1.2), explode=explode,
        wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white'})

#ajoue de text
plt.text(0.5,1.2,"97.1%",
         fontsize=40,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
plt.text(2.4,1.4,"1.4%",
         fontsize=28,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
plt.text(2.4,1.25,"1.5%",
         fontsize=28,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
#plt.title('Store Inventory')
#plt.ylabel('Product')
#plt.xlabel('Quantity')
plt.savefig('key_figure2020.png' ,transparent=True, dpi=300)
plt.show()