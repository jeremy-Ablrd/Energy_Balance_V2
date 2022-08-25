import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import patches


 #########       GENERATE FIGURE         ##########

fig = plt.figure(figsize=(12,9))

 #########      GENERATE DATAFRAME (PIE CHART)  #########

#1st Pie Chart
Energies1 = '','','',''
Generation1 = [52.3, 35.1, 12.4, 0.8]
Colors1 = ['#00b386', '#269393', '#ffb833', '#fff180']
explode1 = (0, 0, 0, 0)

 #########      GENERATE GRAPHIQUE      ##########

plt.pie(x=Generation1, labels=Energies1, colors=Colors1,
        labeldistance=1.1, #or None
        #explode=explode1,
        autopct=None, #or None
        shadow=False, startangle=-0, counterclock=False, frame=False,
       #center=(1.2,1.2),
        wedgeprops = { 'linewidth' : 1, 'edgecolor' : 'white' },
        textprops = {'fontsize': 13, 'color': 'black'},
        )

#plt.title('Store Inventory')
#plt.ylabel('Product')
#plt.xlabel('Quantity')

 ########       SAVE FIGURE     ##########

#plt.savefig('Elect_Consump.png', transparent=True, dpi=300)
plt.show()