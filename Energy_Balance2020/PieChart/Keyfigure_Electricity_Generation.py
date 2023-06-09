import pandas as pd
import matplotlib.pyplot as plt

'''
Deux graphiques en sortie de ce code, il suffit uniquement de mettre en entrer le tableau en entier
et le code fera automatiquement le calcule de la somme des carburants.
'''

# ------- Données d'entrée ------- #
filename = "Seychelles Energy Balance For 2020 - ver3.xlsx"     # nom du fichier excel
excel_sheet_name = "Electricity Stat-2020"        # nom de la feuille de calcule
position_line_header = 37                       # numéro de la ligne de l'entête du tableau
nb_rows = 5                                     # nombre de lignes sans compter l'entête
nb_cols = 3                                     # nombre de colonnes

name_figure1 = "Electricity Generation Fuel Breakdown"
name_figure2 = "Electricity Generation Summary"

color_elect_gene_breakdown = ['#007F7F', '#42A0A0', '#FAD335', '#A3B825']
color_elect_gene = ['#007F7F', '#FAD335', '#A3B825']


def generation_chart(dataframe, title, color=None):
    ax = dataframe.plot(kind='pie', y='GWh', counterclock=False, labels=None, colors=color, figsize=(9, 9))
    plt.title(title)
    plt.ylabel('')
    ax.get_legend().remove()
    title_split = title.split(' ')
    title_figure = '_'.join(title_split)
    plt.savefig(f'Figure_{title_figure}' + '.png', transparent=True, dpi=300)


# --- programme principale --- #
path = f"../{filename}"
file = pd.read_excel(path, sheet_name=excel_sheet_name, header=position_line_header-1)
df = file.iloc[0:nb_rows, 0:nb_cols]

# --- modification dataframe --- #
df['GWh'][2] = 5.70889
df['GWh'][3] = 4.032839
df.drop(index=4, inplace=True)
total = sum([i for i in df['GWh']])
df['Share'] = [round(i/total, 3) for i in df['GWh']]
print("DATAFRAME 'df' :\n", df)
print("TOTAL :", total)

df_modify = df.copy()
sum_fuel = df_modify['GWh'][0] + df_modify['GWh'][1]
sum_share = df_modify['Share'][0] + df_modify['Share'][1]
df_fuel = pd.DataFrame(data=[('Fuel Oil', sum_fuel, sum_share)], columns=['Technology', 'GWh', 'Share'])
df_modify.drop([0, 1], axis=0, inplace=True)
df_modify = pd.concat([df_fuel, df_modify], axis=0).reset_index(drop=True)

print()
print("DATAFRAME 'df_modify' : \n", df_modify)

graphic = [(df, name_figure1, color_elect_gene_breakdown), (df_modify, name_figure2, color_elect_gene)]

for graph in graphic:
    generation_chart(graph[0], graph[1], graph[2])
plt.show()
