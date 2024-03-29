import pandas as pd
import numpy as np
from Function_PieChart_Electricity_Gen import *
from Function_PieChart_PEC_FEC import *

# -------  Config for FINAL ENERGY CONSUMPTION ------- #

# Read .xlsx (excel file) ; sheet_name = "Energy Balance-2021"
path = "C:/Users/jerem/PycharmProjects/pythonProject/Infography/Energy_Balance2021/Seychelles Energy Balance For 2021 - ver2 2.xlsx"
file = pd.read_excel(path, sheet_name="Energy Balance-2021", header=76)

# create Dataframe "df" for the concerned table [FINAL ENERGY CONSUMPTION (FEC)]
df = file.iloc[0:10, 0:3]

# -------------- Sorted DataFrame descending -------------- #
df_sorted = df.sort_values('TOE', ascending=False)

df_values = []                  # get values
for values in df_sorted.values:
    df_values.append(values)

df_keys = []                    # get columns
for columns in df_sorted.columns:
    df_keys.append(columns)

new_df = pd.DataFrame(df_values, columns=df_keys)
# -------------------------------------------------------- #

# Config global data parameters
energy_glob = new_df['Energy Form']
value_energy = new_df['TOE']
share = new_df['Share']
total_TOE = file.loc[10][1]
print("Total :", total_TOE, "TOE")

# Create new column for percentage of 'Share'
share_percent = np.array([])
for i in share.values:
    share_percent = np.append(share_percent, round(i*100, 2))
new_df.insert(3, 'Share %', share_percent, allow_duplicates=False)
print(new_df)

# -------  Config Data FEC (2 charts) ------- #

# data (1st Chart)
energy1 = energy_glob[0:6]
label_print_chart1 = ['', '', '', f'{energy1[3]}({share_percent[3]}%)', f'{energy1[4]}({share_percent[4]}%)',
                      f'{energy1[5]}({share_percent[5]}%)', '']
value_percent1 = np.append(share_percent[0:6], sum(share_percent[6:11]))
print("Energy 1 tech:", energy1.tolist())        # add wind for close the chart
print("% values for 1st chart:", value_percent1)

# config (1st Chart)
colors1 = ['#00b386', '#269393', '#42a1a1', '#67b3b3', '#bbdddd', '#ffffff', '#ffcc00']
explode1 = (0.001, 0.01, 0.01, 0.01, 0.01, 0.01, 0.1)
label_dist1 = 1.1
wedges1 = {'linewidth': 1, 'edgecolor': 'white'}
text1 = {'fontsize': 17, 'color': 'black'}

# 2nd data pie chart [ Sorted DATA for obtain chart descending ]
# data (2nd Chart)
energy2 = energy_glob[6:10]
label_print_chart2 = ['', '', '', f'{energy2[9]}({share_percent[9]}%)']
value_chart2 = value_energy[6:10]
print("Energy 2 tech:", energy2.tolist())        # add wind for close the chart
print("% values for 2nd chart:", new_df['Share %'][6:10].tolist())

# config (2nd Chart)
colors2 = ['#ffa600', '#ffb833', '#ffc966', '#ffdb99']
explode2 = (0.001, 0.01, 0.01, 0.01)
label_dist2 = 0.25
wedges2 = {'linewidth': 1, 'edgecolor': 'white'}
text2 = {'fontsize': 17, 'color': 'black'}

# ------- Function Chart ------- #

fig = figure(20, 9)
chart_1 = Chart(1, 2, 1)                # get subplot chart1 by Class (inside other .py)
chart_2 = Chart(1, 2, 2)                # get subplot chart2 by Class (inside other .py)
subplot1 = chart_1.pie_chart(value_percent1, label_print_chart1, colors1, explode1, label_dist1, wedges1, text1)
subplot2 = chart_2.pie_chart(value_chart2, label_print_chart2, colors2, explode2, label_dist2, wedges1, text1)

# ------- Function Text ------- #

print_text(-2.9, -0.4, str(energy_glob[0]) + "\n" + f"({str(round(share_percent[0]))}%)", 27, "black", "top", "center")
print_text(-3.6, 0.25, str(energy_glob[1]) + "\n" + f"({str(round(share_percent[1]))}%)", 27, "black", "top", "center")
print_text(-2.95, 0.7, str(energy_glob[2]) + "\n" + f"({str(round(share_percent[2]))}%)", 26, "black", "top", "center")
print_text(0.1, -0.35, str(energy_glob[6]) + "\n" + f"({str(share_percent[6])}%)", 27, "black", "top", "center")
print_text(-0.5, 0.27, str(energy_glob[7]) + "\n" + f"({str(share_percent[7])}%)", 26, "black", "top", "center")
print_text(0.3, 0.6, str(energy_glob[8]) + "\n" + f"({str(share_percent[8])}%)", 26, "black", "top", "center")

# ------- Print Chart------- #

plt.savefig('FEC2021.png', transparent=True, dpi=300)
plt.show()
