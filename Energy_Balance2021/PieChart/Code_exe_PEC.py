import pandas as pd
import numpy as np
from Function_PieChart_Electricity_Gen import *
from Function_PieChart_PEC_FEC import *

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
    share_percent.append(round(i*100, 2))
share_percent = np.array(share_percent)
print("% share :", share_percent)

# -------  Config Data PEC (2 chart) ------- #

# data (1st Chart)
energy1 = energy_glob[0:6]
label_print_chart1 = ['', '', '', f'{energy1[3]}({share_percent[3]}%)', f'{energy1[4]}({share_percent[4]}%)', '']
value_percent1 = np.append(share_percent[0:5], sum(share_percent[5:11]))
print("Energy 1 tech:", energy1.tolist())        # add wind for close the chart
print("% values for 1st chart:", value_percent1)

# config (1st Chart)
colors1 = ['Teal', '#269393', '#42a1a1', '#67b3b3', '#bbdddd', '#ffa600']
explode1 = (0.001, 0.01, 0.01, 0.01, 0.01, 0.1)
label_dist1 = 1.1
wedges1 = {'linewidth': 1, 'edgecolor': 'white'}
text1 = {'fontsize': 13, 'color': 'black'}

# 2nd data pie chart [ Sorted DATA for obtain chart descending ]
# Creating a new DataFrame sorted for print chart ascending
# ----------------------------------- #
df_sorted = df[5:11].sort_values('TOE', ascending=False)

df_values = []                  # get values
for values in df_sorted.values:
    df_values.append(values)

df_keys = []                    # get columns
for columns in df_sorted.columns:
    df_keys.append(columns)

new_df = pd.DataFrame(df_values, columns=df_keys)       # make new DataFrame with good indexes
print(new_df)
# ----------------------------------- #
share_percent_sorted = []
for share in df_sorted['Share']:
    share_percent_sorted.append(round(share*100, 2))
print(share_percent_sorted)

# data (2nd Chart)
energy2 = new_df['Energy Form']

label_print_chart2 = ['', '', f'{energy2[2]}({share_percent_sorted[2]}%)', f'{energy2[3]}({share_percent_sorted[3]}%)',
                      f'{energy2[4]}({share_percent_sorted[4]}%)', f'{energy2[5]}({share_percent_sorted[5]}%)']
value_chart2 = value_energy[5:11].sort_values(ascending=False)      # for print chart sorted descending

# config (2nd Chart)
colors2 = ['#ffa600', '#ffb833', '#ffc966', '#ffd280', '#ffdb99', '#ffedcc']
explode2 = (0.001, 0.01, 0.01, 0.01, 0.01, 0.01)
label_dist2 = 1.05
wedges2 = {'linewidth': 1, 'edgecolor': 'white'}
text2 = {'fontsize': 12, 'color': 'black'}

# ------- Function Chart ------- #

fig = figure(20, 9)
chart_1 = Chart(1, 2, 1)                # get subplot chart1 by Class (inside other .py)
chart_2 = Chart(1, 2, 2)                # get subplot chart2 by Class (inside other .py)
subplot1 = chart_1.pie_chart(value_percent1, label_print_chart1, colors1, explode1, label_dist1, wedges1, text1)
subplot2 = chart_2.pie_chart(value_chart2, label_print_chart2, colors2, explode2, label_dist1, wedges1, text1)

# ------- Function Text ------- #

print_text(-3.02, -0.4, str(energy_glob[0]) + "\n" + f"({str(round(share_percent[0]))}%)", 20, "black", "top", "center")
print_text(-3.4, 0.6, str(energy_glob[1]) + "\n" + f"({str(round(share_percent[1]))}%)", 20, "black", "top", "center")
print_text(-2.5, 0.55, str(energy_glob[2]) + "\n" + f"({str(round(share_percent[2]))}%)", 17, "black", "top", "center")
print_text(-0.4, 0.45, str(energy_glob[5]) + "\n" + f"({str(share_percent[5])}%)", 20, "black", "top", "center")
print_text(0.05, -0.4, str(energy_glob[6]) + "\n" + f"({str(share_percent[6])}%)", 20, "black", "top", "center")

# ------- Print Chart------- #

plt.savefig('PEC2021.png', transparent=True, dpi=300)
plt.show()
