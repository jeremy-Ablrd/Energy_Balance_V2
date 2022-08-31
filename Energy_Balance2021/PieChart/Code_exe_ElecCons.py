import pandas as pd
import numpy as np
from Function_PieChart_Electricity_Gen import *
from Function_PieChart_PEC_FEC import *

# -------  Config for SECTORIAL ENERGY CONSUMPTION ------- #

# Build DataFrame
data = {'Domestic': 138745369,
        'Industry & Commercial': 207422855,
        'Government': 55489598 - 1019437,
        'Street Lights':  1019437}

df = pd.DataFrame(data.values(), index=data.keys(), columns=['TOE'])
df = df.sort_values('TOE', ascending=False)
print(df)

# 1st Pie Chart
sectors = df.index.tolist()
generation = df['TOE']
colors1 = ['#00b386', '#269393', '#ffb833', '#fff180']
explode1 = (0, 0, 0, 0)
label_dist = 1.1
wedge = {'linewidth': 1, 'edgecolor': 'white' }
text = {'fontsize': 13, 'color': 'black'}
print(sectors)
print(generation)

# ------- GENERATE GRAPHIQUE ------- #

figure(12, 9)
pie_chart(generation, None, colors1, explode1, label_dist, wedge, text)

# ------- SAVE FIGURE ------- #

plt.savefig('Elect_Consump2021.png', transparent=True, dpi=300)
plt.show()
