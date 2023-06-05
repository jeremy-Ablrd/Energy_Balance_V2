import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import DataFrame

"""Information importante :
Ce dataframe correspond aux données sur la consommation d'énergie dans différent secteur.
Il y a deux types de graphiques qui est générés dans ce code :
- sur les données sectorial en barre horizontale,
- sur les données selon le type de transport en anneau. 
  Les noms pour chaque ne sont pas visibles, l'ordre (de haut en bas) est la même que celui du dataframe.
"""

# ------- BAR CHART FOR ENERGY SECTORIAL CONSUMPTION ------- #
filename = "Seychelles Energy Balance For 2019 - ver5.xlsx"
excel_sheet_name = "Energy Balance-2019"        # nom de la feuille de calcule
position_line_header = 99                       # numéro de la ligne de l'entête du tableau
nb_rows = 8                                     # nombre de lignes sans compter l'entête
nb_cols = 3                                     # nombre de colonnes

colors_bar_chart = ['#52A8A8', '#00b386', '#A3B825', '#D1C420', '#ff8c00']            # correspond aux couleurs associer au graphique à barre horizontale
colors_pie_chart = ['#494f56', '#018080', '#2b489d']                                  # correspond aux couleurs associer au graphique en camembert pour le secteur du transport

filename_bar_chart = 'Sectorial_Consump_2019'                              # nom du fichier de sauvegarde ; les espaces sont à éviter, mettre des "_" à la place.
filename_pie_chart = 'RingChart_Transport_2019'


def make_dataframe(df: DataFrame, bar_h=True):
    # Rename index
    n_index = []
    for i in range(0, len(df)):
        n_index.append(i)
    df.index = n_index
    print("Dataframe Sectorial : \n", df)

    share_percent = []
    if bar_h:
        # Share in % values
        for i in df['Share']:
            share_percent.append(round(i*100, 1))
        label = df['SECTOR'].str.lower().str.title()  # str.lower()/upper()/title() change the letter minuscule, capital...
    else:
        for i in df['TOE'][1:4]:
            operation = (i / df['TOE'][0]) * 100
            share_percent.append(round(operation, 1))
        label = df['SECTOR'][1:4]

    share_percent = np.array(share_percent)
    print(list(zip(label, share_percent)))
    return label, share_percent


def generate_bar_h(sector_name, share, colors):
    global filename_bar_chart
    # --------- Création de la Figure --------- #
    fig = plt.figure(figsize=(12, 4))
    ax = fig.add_subplot(111)

    # ----------- création du graphique ----------- #
    plt.barh(sector_name, width=share, height=0.6, color=colors)

    # ----------- AXE CONFIGURATION ----------- #
    for side in ['top', 'bottom', 'left', 'right']:
        ax.spines[side].set_visible(False)

    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_ticks_position('top')
    ax.tick_params(labelsize=20, length=0)

    ax.xaxis.set_tick_params(pad=5)
    ax.yaxis.set_tick_params(pad=10)

    ax.grid(visible=True, color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)

    ax.invert_yaxis()
    for a in ax.patches[:-1]:
        plt.text(a.get_width() - 4, a.get_y() + 0.46,
                 s=str(round((a.get_width()), 2)) + '%',
                 fontsize=15, fontweight='bold',
                 color='black')
    for a in ax.patches[4:5]:
        plt.text(a.get_width(), a.get_y() + 0.46,
                 s=str(round((a.get_width()), 2)) + '%',
                 fontsize=15, fontweight='bold',
                 color='black')

    # ----------- sauvegarde et affichage ----------- #
    plt.savefig(filename_bar_chart + '.png', transparent=True, dpi=300)


def chart(name, value, color=None):
    plt.figure(figsize=(12, 9))
    plt.pie(x=value, labels=name, colors=color, labeldistance=None,
            # explode=explode2,
            pctdistance=0.85,
            autopct='%2.0f%%', shadow=False, startangle=-0, counterclock=False, frame=False,
            wedgeprops={'linewidth': 2, 'edgecolor': 'white'},
            textprops={'fontsize': 27, 'color': 'white'}
            # center=(1.2,1.2)
            )
    circle = plt.Circle((0, 0), 0.7, color='white')
    p = plt.gcf()
    p.gca().add_artist(circle)
    plt.axis('equal')
    plt.savefig(filename_pie_chart + '.png', transparent=True, dpi=300)


# ---- PROGRAMME PRINCIPALE ---- #
absolute_path = os.getcwd()
path = f"../{filename}"
file = pd.read_excel(path, sheet_name=excel_sheet_name, header=position_line_header-1)

dataframe = file.iloc[0:nb_rows, 0:nb_cols]
print("Entire DataFrame : \n", dataframe)
print()

df_bar_h = dataframe.drop([1, 2, 3], axis=0)

df_transport = dataframe.iloc[0:4]
print("DataFrame only for Transport sector : \n", df_transport)
print()

total = file.loc[nb_rows][0:nb_cols]
print("TOTAL : \n", total)
print()


label1, data1 = make_dataframe(df_bar_h)
generate_bar_h(label1, data1, colors_bar_chart)

label2, data2 = make_dataframe(df_transport, False)
chart(label2, data2, colors_pie_chart)
plt.show()
