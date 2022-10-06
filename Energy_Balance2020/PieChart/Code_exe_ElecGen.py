import pandas as pd
import numpy as np
from Function_PieChart_Electricity_Gen import *

#-------  CHART FOR ELECTRICITY GENERATION ------- #

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

# ------------- CONFIG DATA FOR CHART ------------- #

# Config chart
colors_share = ['Teal', '#42a1a1', '#a3b825', '#fad335']
gap = (0, 0, 0.1, 0.1)
print(share_percent)

# ---------------- CALL FUNCTION ---------------- #

# Call function figure(length, width):
figure(12, 9)

# Call function pie_chart(x, labels, colors, explode)
pie_chart(value_energy, energy, colors_share, gap)

# Call function print_text(x, y, txt, fontsize, color, verti_align, horiz_align, bbox=None)
print_text(0.7, 1.2, str(share_percent[0]) + "%", 30, "black", 'top', 'center')         #Heavy Fuel Oil
print_text(1.8, 1.55, str(share_percent[1]) + "%", 28, "black", 'top', 'center')        #Light ""    ""
print_text(2.5, 1.45, str(share_percent[2]) + "%", 25, "black", 'top', 'center')        #Wind
print_text(2.5, 1.30, str(share_percent[3]) + "%", 25, "black", 'top', 'center',)       #Solar

plt.savefig('Electgene2020.png', transparent=True, dpi=300)
plt.show()
