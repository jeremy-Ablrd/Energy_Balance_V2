import pandas as pd
import numpy as np
from Function_PieChart_Electricity_Gen import *
import matplotlib.pyplot as plt

#-------  CHART FOR KEY FIGURE ELECTRICITY ------- #

# Read .xlsx (excel file) ; sheet_name = "Electricity Stat-2020"
path = "C:/Users/jerem/Desktop/Energy_Balance_V2/Energy_Balance2020/Seychelles Energy Balance For 2020 - ver2.xlsx"
file = pd.read_excel(path, sheet_name="Electricity Stat-2020", header=36)

# create Dataframe "df" for the table concerned [ELECTRICITY GENERATION MIX IN PUC]
df = file.iloc[0:5, 0:3]
print(df)

# Config data parameters
energy = df['Technology'].iloc[0:4]
value_energy = df['GWh'].iloc[0:4]
share = df["Share"].iloc[0:4]
total_energy = df.loc[4][1]
print("Total energy in GWh :", total_energy)

# Change share values to percent
share_percent = []
for i in share.values:
    share_percent.append(round(i*100, 1))
share_percent = np.array(share_percent)

# ------------- CONFIG DATA  ------------- #

# Config data
energy_key = ['Fuel Oil', energy[2], energy[3]]
value_percent = [round(share_percent[0] + share_percent[1], 1), share_percent[2], share_percent[3]]

print(list(zip(energy_key, value_percent)))

# Config pie chart
colors_share = ['Teal', '#a3b825', '#fad335']
gap = (0.15, 0, 0)

# ---------------- CALL FUNCTION ---------------- #

# Call function figure(length, width):
figure(12, 9)

# Call function pie_chart(x, labels, colors, explode)
pie_chart(value_percent, energy_key, colors_share, gap)

# Call function print_text(x, y, txt, fontsize, color, verti_align, horiz_align, bbox=None)
print_text(0.6, 1.2, str(value_percent[0]) + "%", 37, "black", 'top', 'center')         #Fuel oil
print_text(2.5, 1.4, str(value_percent[1]) + "%", 25, "black", 'top', 'center')         #Wind
print_text(2.5, 1.25, str(value_percent[2]) + "%", 25, "black", 'top', 'center',)       #Solar

plt.savefig('key_figure2020.png', transparent=True, dpi=300)
plt.show()
