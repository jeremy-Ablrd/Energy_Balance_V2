import pandas as pd
import numpy as np
from Function_PieChart_Electricity_Gen import *
from Func_PieChart_PEC_FEC import *

# -------  Config for PRIMARY ENERGY CONSUMPTION ------- #

# Read .xlsx (excel file) ; sheet_name = "Energy Balance-2021"
path = "C:/Users/jerem/PycharmProjects/pythonProject/Infography/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2021", header=44)

# create Dataframe "df" for the concerned table [PRIMARY ENERGY CONSUMPTION (PEC)]
df = file.iloc[0:12, 0:3]
print(df)
# Config data parameters

energy_glob = df['Energy Form'].iloc[0:11]
value_energy = df['TOE'].iloc[0:11]
share = df['Share'].iloc[0:11]
total_TOE = df.loc[11][1]

# Change share values to percent
share_percent = []
for i in share.values:
    share_percent.append(round(i*100, 1))
share_percent = np.array(share_percent)
print("% share :", share_percent)

# -------  Config Data PEC (2 chart) ------- #

# 1st data pie chart
energy1 = energy_glob[0:6]
label_print_chart1 = '', '', '', 'LPG(3.28%)', 'Jet A1(2.27%)', ''
value_percent1 = np.append(share_percent[0:5], sum(share_percent[5:11]))
print("Energy 1 tech:", energy1.tolist())        # add wind for close the chart
print("% values for 1st chart:", value_percent1)

colors1 = ['Teal', '#269393', '#42a1a1', '#67b3b3', '#bbdddd', '#ffa600']
explode1 = (0.001, 0.01, 0.01, 0.01, 0.01, 0.1)
label_dist1 = 1.1
wedges1 = {'linewidth': 1, 'edgecolor': 'white'}
text1 = {'fontsize': 13, 'color': 'black'}

# 2nd data pie chart
energy2 = energy_glob[5:11]
label_print_chart2 = '', '', 'Solar Thermal(0.04%)', 'Fuelwood(0.03%)', 'Kerosene(0.01%)', 'Avgas(0.005%)'
value_chart2 = value_energy[5:11].tolist()
print("Energy 2 tech:", energy2.tolist())
print("TOE values for 2st chart:", value_chart2)

colors2 = ['#ffa600', '#ffb833', '#ffc966', '#ffd280', '#ffdb99', '#ffedcc']
explode2 = (0.001, 0.01, 0.01, 0.01, 0.01, 0.01)
label_dist2 = 1.05
wedges2 = {'linewidth': 1, 'edgecolor': 'white'}
text2 = {'fontsize': 12, 'color': 'black'}

# ------- Function Chart ------- #

fig = figure(14, 9)
chart_1 = Chart(1, 2, 1)
chart_2 = Chart(1, 2, 2)
subplot1 = chart_1.pie_chart(value_percent1, label_print_chart1, colors1, explode1, label_dist1, wedges1, text1)
subplot2 = chart_2.pie_chart(value_chart2, label_print_chart2, colors2, explode2, label_dist1, wedges1, text1)

# ------- Function Text ------- #

print_text(-3.0, -0.4, str(energy_glob[0]) + "\n" + str(share_percent[0]) + "%", 20, "black", "top", "center")
print_text(-3.4, 0.6, str(energy_glob[1]) + "\n" + str(share_percent[1]) + "%", 20, "black", "top", "center")
print_text(-2.5, 0.55, str(energy_glob[2]) + "\n" + str(share_percent[2]) + "%", 14, "black", "top", "center")
print_text(-0.5, 0.2, str(energy_glob[5]) + "\n" + str(share_percent[5]) + "%", 20, "black", "top", "center")
print_text(0.3, -0.4, str(energy_glob[6]) + "\n" + str(share_percent[6]) + "%", 20, "black", "top", "center")

# ------- Print Chart------- #

plt.savefig('PEC2021.png', transparent=True, dpi=300)
plt.show()