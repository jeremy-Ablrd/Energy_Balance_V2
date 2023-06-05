import pandas as pd
import numpy as np
from Function_PieChart_Electricity_Gen import *
import matplotlib.pyplot as plt

# -------  CHART FOR KEY FIGURE ELECTRICITY ------- #

# Read .xlsx (excel file) ; sheet_name = "Electricity Stat-2020"
path = "C:/Users/jerem/Documents/Work_SEC_VSI/Dossier-VSI_Graph/Energy_Balance_V2/Energy_Balance2020/Seychelles Energy Balance For 2020 - ver3.xlsx"
file = pd.read_excel(path, sheet_name="Electricity Stat-2020", header=36)


def total_dataframe(data_frame):
    data_frame['GWh'][-1:] = sum(data_frame['GWh'][:-1])
    return data_frame


df = file.iloc[0:5, 0:3]
df['GWh'][3] = 5.719
df['Share'] = [round(i/df['GWh'][4], 3) for i in df['GWh']]
df.drop(index=4, inplace=True)
print(df)

df_modify = df.copy()
sum_fuel = df_modify['GWh'][0] + df_modify['GWh'][1]
sum_share = df_modify['Share'][0] + df_modify['Share'][1]
df_fuel = pd.DataFrame(data=[('Fuel Oil', sum_fuel, sum_share)], columns=['Technology', 'GWh', 'Share'])
df_modify.drop([0, 1], axis=0, inplace=True)
df_modify = pd.concat([df_fuel, df_modify], axis=0).reset_index(drop=True)

print(df_modify)

colors_share2 = ['#007F7F', '#FAD335', '#A3B825']

colors_share1 = ['#007F7F', '#42A0A0', '#FAD335', '#A3B825']


ax1 = df.plot(kind='pie', y='GWh', counterclock=False, labels=None, colors=colors_share1, figsize=(9, 9))
plt.title("Elect Generation Fuel Breakdown")
plt.ylabel('')
ax1.get_legend().remove()
path_savefig = "C:/Users/jerem/Documents/Work_SEC_VSI/Dossier-VSI_Graph/Energy_Balance_V2/Correction_Energy_Balance"
plt.savefig(f'{path_savefig}/Electricity_generation_breakdown2020.png', transparent=True, dpi=300)


ax = df_modify.plot(kind='pie', y='GWh', counterclock=False, labels=None, colors=colors_share2, figsize=(9, 9))
plt.title("Elect Generation Summary")
plt.ylabel('')
ax.get_legend().remove()

path_savefig = "C:/Users/jerem/Documents/Work_SEC_VSI/Dossier-VSI_Graph/Energy_Balance_V2/Correction_Energy_Balance"
plt.savefig(f'{path_savefig}/Electricity_generation_summary2020.png', transparent=True, dpi=300)
plt.show()

# # Config data parameters
# energy = df['Technology'].iloc[0:4]
# value_energy = df['GWh'].iloc[0:4]
# share = df["Share"].iloc[0:4]
# total_energy = df.loc[4][1]
# print("Total energy in GWh :", total_energy)



# # Change share values to percent
# share_percent = []
# for i in share.values:
#     share_percent.append(round(i*100, 1))
# share_percent = np.array(share_percent)
#
# # ------------- CONFIG DATA  ------------- #
#
# # Config data
# energy_key = ['Fuel Oil', energy[2], energy[3]]
# value_percent = [round(share_percent[0] + share_percent[1], 1), share_percent[2], share_percent[3]]
#
# print(list(zip(energy_key, value_percent)))
#
# # Config pie chart
# colors_share = ['Teal', '#a3b825', '#fad335']
# gap = (0.15, 0, 0)
#
# # ---------------- CALL FUNCTION ---------------- #
#
# # Call function figure(length, width):
# figure(12, 9)
#
# # Call function pie_chart(x, labels, colors, explode)
# pie_chart(value_percent, energy_key, colors_share, gap)
#
# # Call function print_text(x, y, txt, fontsize, color, verti_align, horiz_align, bbox=None)
# print_text(0.6, 1.2, str(value_percent[0]) + "%", 37, "black", 'top', 'center')         #Fuel oil
# print_text(2.5, 1.4, str(value_percent[1]) + "%", 25, "black", 'top', 'center')         #Wind
# print_text(2.5, 1.25, str(value_percent[2]) + "%", 25, "black", 'top', 'center',)       #Solar
#
# # plt.savefig('key_figure2020.png', transparent=True, dpi=300)
# plt.show()
