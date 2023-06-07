import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from Function_PieChart_Electricity_Gen import *

# --- Configuration manuel--- #
filename = "Seychelles Energy Balance For 2019 - ver5.xlsx"     # nom du fichier excel
excel_sheet_name = "Electricity Stat-2019"        # nom de la feuille de calcule
position_line_header = 34                       # numéro de la ligne de l'entête du tableau
nb_rows = 5                                     # nombre de lignes sans compter l'entête
nb_cols = 3                                     # nombre de colonnes

colors_share = ['Teal', '#42a1a1', '#a3b825', '#fad335']
gap = (0, 0, 0.1, 0.1)
position_label = [(0.7, 1.2, 30), (1.8, 1.55, 28), (2.5, 1.45, 25), (2.5, 1.30, 25)]        # dans la parenthèse = (x, y, taille du texte), Le positionnement du texte doit être modifier pour chaque
# graphique.


# --- Fonction --- #
def print_text(x: float, y: float, txt: str, fontsize: int, color: str, verti_align: str, horiz_align: str):
    plt.text(x, y, txt, fontsize=fontsize, color=color, verticalalignment=verti_align,
             horizontalalignment=horiz_align,)


# --- Programme principale --- #
path = f"../{filename}"
file = pd.read_excel(path, sheet_name=excel_sheet_name, header=position_line_header-1)

# données du tableau "ELECTRICITY GENERATION MIX IN PUC"
df = file.iloc[0:nb_rows, 0:nb_cols]
print(df)

# configuration des données
energy = df['Technology'].iloc[0:4]
value_energy = df['GWh'].iloc[0:4]
share = df["Share"].iloc[0:4]
total_energy = df.loc[4][1]
print("Total energy in GWh :", total_energy)

# mettre les valeurs en pourcentage
share_percent = []
for i in share.values:
    share_percent.append(round(i*100, 1))
share_percent = np.array(share_percent)
print(list(zip(energy, share_percent)))

# ---------------- CALL FUNCTION ---------------- #

plt.figure(figsize=(12, 9))

# Call function pie_chart(x, labels, colors, explode)
plt.pie(x=value_energy, labels=None, colors=colors_share, explode=gap, labeldistance=None,
        wedgeprops=None,
        textprops=None,
        autopct=None, shadow=False, startangle=-0, counterclock=False, frame=False,
        center=(1.2, 1.2))

for i, data in enumerate(position_label):
    print_text(data[0], data[1], str(share_percent[i]) + "%", data[2], "black", 'top', 'center')

plt.savefig('Figure_Electricity_generation_2019.png', transparent=True, dpi=300)
plt.show()
