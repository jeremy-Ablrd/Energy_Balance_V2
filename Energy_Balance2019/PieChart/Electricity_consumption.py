import pandas as pd
from Function_PieChart_PEC_FEC import *

# --- creation de la base de donnée --- #
data = {'Domestic': 134538602,
        'Industry & Commercial': 217309119,
        'Government': 26368176,
        'Street Lights': 1144319}

# --- paramètre graphique --- #
colors = ['#00b386', '#269393', '#ffb833', '#fff180']
explode = (0, 0, 0, 0)
label_distance = 1.1

# ---- création Dataframe avec data ---- #
df = pd.DataFrame(data.values(), index=data.keys(), columns=['TOE'])
df = df.sort_values('TOE', ascending=False)
print()
print('DATAFRAME "data" :\n', df)
print()

# 1st Pie Chart
sectors = df.index.tolist()
generation = df['TOE']

wedge = {'linewidth': 1, 'edgecolor': 'white'}
text = {'fontsize': 13, 'color': 'black'}

values_percent = []
for data in generation:
    operation = round((data/sum(generation)) * 100, 1)
    values_percent.append(operation)

print(list(zip(sectors, values_percent)))

# ------- GENERATE GRAPHIQUE ------- #

plt.figure(figsize=(12, 6))

plt.pie(x=generation, labels=None, colors=colors, explode=explode, labeldistance=label_distance,
        wedgeprops=wedge,
        textprops=text,
        autopct=None, shadow=False, startangle=-0, counterclock=False, frame=False,
        center=(1.2, 1.2))


# ------- SAVE FIGURE ------- #

plt.savefig('Figure_ Electricity_Consumption_2019.png', transparent=True, dpi=300)
plt.show()
