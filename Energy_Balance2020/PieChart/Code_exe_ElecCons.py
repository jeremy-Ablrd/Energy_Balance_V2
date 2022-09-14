import pandas as pd
from Function_PieChart_Electricity_Gen import *
from Function_PieChart_PEC_FEC import *

# -------  Config for SECTORIAL ENERGY CONSUMPTION ------- #

# Build DataFrame
data = {'Domestic': 140994699,
        'Industry & Commercial': 210140066,
        'Government': 26714346,
        'Street Lights': 1081675}

df = pd.DataFrame(data.values(), index=data.keys(), columns=['TOE'])
df = df.sort_values('TOE', ascending=False)
print(df)

# 1st Pie Chart
sectors = df.index.tolist()
generation = df['TOE']
colors1 = ['#00b386', '#269393', '#ffb833', '#fff180']
explode1 = (0, 0, 0, 0)
label_dist = 1.1
wedge = {'linewidth': 1, 'edgecolor': 'white'}
text = {'fontsize': 13, 'color': 'black'}

values_percent = []
for data in generation:
    operation = round((data/sum(generation)) * 100, 1)
    values_percent.append(operation)

print(list(zip(sectors, values_percent)))

# ------- GENERATE GRAPHIQUE ------- #

figure(12, 9)
pie_chart(generation, None, colors1, explode1, label_dist, wedge, text)

# ------- SAVE FIGURE ------- #

plt.savefig('Elect_Consump2020.png', transparent=True, dpi=300)
plt.show()
