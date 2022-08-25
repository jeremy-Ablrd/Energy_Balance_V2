import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import pandas as pd
import seaborn as sns


# Appel du Fichier
path = "C:/Users/jerem/PycharmProjects/pythonProject/Infography/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2021", header=2, index_col=[0, 14])
df = file.iloc[1:36, 1:14]


# Pretraitement -> où tirer les data, traiter les data avant config

# Générer figure

# "   "   data

# Show

'''#generate figure
plt.figure(figsize=(12, 9))

#generate dataframe for pie plot
Energies = 'Diesel - Heavy Fuel Oil', 'Diesel - Lite Fuel Oil', 'Solar PV', 'Wind Farm'
Electricity_Generation = [86.7, 10.41, 1.35, 1.54]
Colors = ['Teal', '#42a1a1', '#ffde59', '#ff8c00']
explode = (0, 0, 0.3, 0.3)
#generate graphique

#plt.plot(x,y)
plt.axis([0, 2.4, 0, 2.4])
plt.pie(x= Electricity_Generation, labels= Energies, labeldistance=None, colors= Colors,
        autopct=None, shadow=False, startangle=-0, counterclock=False, frame=False, center=(1.2,1.2), explode=explode)

#ajoue de text
plt.text(0.7,1.2,"86.7%",
         fontsize=30,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
plt.text(1.8,1.5,"10.4%",
         fontsize=28,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
plt.text(2.70,1.30,"1.4%",
         fontsize=25,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )
plt.text(2.70,1.48,"1.5%",
         fontsize=25,
         color="black",
         verticalalignment ='top',
         horizontalalignment ='center',
         bbox =None
        )


#plt.title('Store Inventory')
#plt.ylabel('Product')
#plt.xlabel('Quantity')
plt.savefig('Electgene2020.png' ,transparent=True, dpi=300)
plt.show()'''